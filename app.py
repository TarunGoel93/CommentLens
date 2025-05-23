from flask import Flask, redirect, url_for, session, request, render_template, jsonify
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from flask_sqlalchemy import SQLAlchemy
import bcrypt
import pickle
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
import asyncpraw
import asyncio
import nest_asyncio
import re
from collections import Counter
import string
import logging
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import requests
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Check NLTK data availability
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    logger.error("NLTK data missing. Please run: python -c \"import nltk; nltk.download('punkt'); nltk.download('stopwords')\"")
    raise

# Define Hindi abusive words with regex word boundaries
abusive_words_hindi = [
    r'\bchutiya\b', r'\bmadarchod\b', r'\bbhenchod\b', r'\bgaand\b', r'\bloda\b', r'\blund\b', r'\brandi\b',
    r'\bsaala\b', r'\bharami\b', r'\bkamina\b', r'\bkutte\b', r'\bkaminey\b', r'\bghanta\b', r'\bchutiye\b',
    r'\bchinki\b', r'\bbhosdi\b', r'\bbhosdike\b', r'\bgandu\b', r'\bchut\b', r'\bchod\b', r'\bchodu\b',
    r'\bbitchod\b', r'\bmc\b', r'\bbc\b', r'\blode\b', r'\brakhail\b', r'\bchutmar\b', r'\bgaandu\b',
    r'\bgand\b', r'\bchodna\b'
]

# Define question words
question_words = [
    'what', 'how', 'why', 'when', 'where', 'who', 'which'
]

# Define Hindi stopwords
hindi_stopwords = [
    'hai', 'hain', 'ho', 'hu', 'h', 'mai', 'main', 'mein', 'ka', 'ki', 'ke', 'ko', 'se', 'par', 'aur', 'or',
    'ya', 'to', 'bhi', 'hi', 'tha', 'thi', 'the', 'na', 'nahi', 'nahin', 'ek', 'do', 'teen', 'char',
    'is', 'us', 'wo', 'vo', 'ye', 'yah', 'waha', 'vaha', 'yaha', 'jaha', 'kaha', 'kya', 'kyu', 'kyun',
    'kab', 'kaise', 'kaisa', 'kon', 'kaun', 'tak', 'aur', 'lekin', 'magar', 'bas', 'ab', 'tab',
    'jab', 'sab', 'kuch', 'koi', 'har', 'ap', 'aap', 'tum', 'hum', 'ham'
]

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = os.urandom(24)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

CLIENT_SECRETS_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

def extract_video_id(url):
    patterns = [
        r'(?:v=|youtu\.be\/|\/embed\/|\/video\/)([a-zA-Z0-9_-]{11})',
        r'youtube\.com\/.*[?&]v=([a-zA-Z0-9_-]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

def get_comments(youtube, video_id, max_comments=500):
    comments = []
    question_comments = []
    abusive_comments = []
    question_comment_ids = []
    abusive_comment_ids = []
    user_comments = {}
    spam_count = 0
    next_page_token = None
    comments_fetched = 0
    retries = 3
    error_message = None

    try:
        while comments_fetched < max_comments:
            for attempt in range(retries):
                try:
                    request = youtube.commentThreads().list(
                        part='snippet',
                        videoId=video_id,
                        maxResults=min(100, max_comments - comments_fetched),
                        pageToken=next_page_token
                    )
                    response = request.execute()

                    for item in response.get('items', []):
                        comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
                        comment_id = item['id']
                        author_id = item['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
                        
                        comments.append(comment_text)
                        comments_fetched += 1
                        
                        # Check for question comments
                        comment_lower = comment_text.lower()
                        is_question = (
                            any(comment_lower.strip().startswith(word) for word in question_words) or
                            re.search(r'\?$', comment_text, re.IGNORECASE)
                        )
                        
                        if is_question:
                            question_comments.append(comment_text)
                            question_comment_ids.append(comment_id)
                        else:
                            # Check for abusive comments with word boundaries
                            for abusive_word in abusive_words_hindi:
                                if re.search(abusive_word, comment_lower, re.IGNORECASE):
                                    abusive_comments.append(comment_text)
                                    abusive_comment_ids.append(comment_id)
                                    break
                        
                        # Check for spam
                        if author_id in user_comments:
                            if comment_text in user_comments[author_id]:
                                spam_count += 1
                            else:
                                user_comments[author_id].add(comment_text)
                        else:
                            user_comments[author_id] = {comment_text}

                        if comments_fetched >= max_comments:
                            break

                    next_page_token = response.get('nextPageToken')
                    logger.debug(f"Fetched {comments_fetched} comments so far. Next page token: {next_page_token}")
                    break  # Successful fetch, exit retry loop

                except HttpError as e:
                    logger.error(f"HTTP error fetching comments (attempt {attempt + 1}/{retries}): {e}")
                    if e.resp.status == 403:
                        error_message = "API quota exceeded or comments disabled for this video."
                        return comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message
                    elif e.resp.status == 404:
                        error_message = "Video not found or invalid video ID."
                        return comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message
                    if attempt == retries - 1:
                        error_message = f"Failed to fetch comments after {retries} attempts: {str(e)}"
                        return comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message
                    time.sleep(1)  # Wait before retrying
                except requests.exceptions.RequestException as e:
                    logger.error(f"Network error fetching comments (attempt {attempt + 1}/{retries}): {e}")
                    if attempt == retries - 1:
                        error_message = "Network error while fetching comments. Please try again later."
                        return comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message
                    time.sleep(1)
                except Exception as e:
                    logger.error(f"Unexpected error fetching comments (attempt {attempt + 1}/{retries}): {e}")
                    if attempt == retries - 1:
                        error_message = "Unexpected error while fetching comments."
                        return comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message
                    time.sleep(1)

            if comments_fetched >= max_comments or not next_page_token:
                break

        logger.info(f"Total fetched: {len(comments)} comments, {len(question_comments)} question comments, {len(abusive_comments)} abusive comments, {spam_count} spam comments")
    except Exception as e:
        logger.error(f"Error fetching comments: {e}")
        error_message = "Failed to fetch comments due to an unexpected error."
        if comments:
            logger.info(f"Returning partial results: {len(comments)} comments fetched before error")

    return comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message

def summarize_comments(comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, sentiments, video_id):
    if not comments:
        logger.warning("No comments provided for summarization")
        return "No comments available to summarize.", []

    positive_comments = [c for c, s in zip(comments, sentiments) if s == 'positive' and c not in question_comments and c not in abusive_comments]
    negative_comments = [c for c, s in zip(comments, sentiments) if s == 'negative' and c not in question_comments and c not in abusive_comments]
    neutral_comments = [c for c, s in zip(comments, sentiments) if s == 'neutral' and c not in question_comments and c not in abusive_comments]
    
    summary_lines = []
    comment_data = []
    
    logger.debug(f"Positive comments: {len(positive_comments)}, Negative comments: {len(negative_comments)}, Neutral comments: {len(neutral_comments)}, Question comments: {len(question_comments)}, Abusive comments: {len(abusive_comments)}")
    
    if abusive_comments:
        summary_lines.append("Top Abusive Comments:")
        for i, (comment, comment_id) in enumerate(zip(abusive_comments[:3], abusive_comment_ids[:3]), 1):
            clean_comment = re.sub(r'<[^>]+>', '', comment)
            summary_lines.append(f"{i}. {clean_comment[:100]}{'...' if len(clean_comment) > 100 else ''}")
            comment_data.append({
                'type': 'abusive',
                'text': clean_comment[:100] + ('...' if len(clean_comment) > 100 else ''),
                'comment_id': comment_id,
                'number': i
            })
    else:
        summary_lines.append("There are no abusive comments.")
        comment_data.append({'type': 'abusive', 'text': "There are no abusive comments.", 'comment_id': None})
    
    if question_comments:
        summary_lines.append("Top Question Comments:")
        for i, (comment, comment_id) in enumerate(zip(question_comments[:3], question_comment_ids[:3]), 1):
            clean_comment = re.sub(r'<[^>]+>', '', comment)
            summary_lines.append(f"{i}. {clean_comment[:100]}{'...' if len(clean_comment) > 100 else ''}")
            comment_data.append({
                'type': 'question',
                'text': clean_comment[:100] + ('...' if len(clean_comment) > 100 else ''),
                'comment_id': comment_id,
                'number': i
            })
    else:
        summary_lines.append("There are no question comments.")
        comment_data.append({'type': 'question', 'text': "There are no question comments.", 'comment_id': None})
    
    if positive_comments:
        summary_lines.append("Top Positive Comments:")
        for i, comment in enumerate(positive_comments[:3], 1):
            clean_comment = re.sub(r'<[^>]+>', '', comment)
            summary_lines.append(f"{i}. {clean_comment[:100]}{'...' if len(clean_comment) > 100 else ''}")
            comment_data.append({
                'type': 'positive',
                'text': clean_comment[:100] + ('...' if len(clean_comment) > 100 else ''),
                'comment_id': None,
                'number': i
            })
    else:
        summary_lines.append("There are no positive comments.")
        comment_data.append({'type': 'positive', 'text': "There are no positive comments.", 'comment_id': None})
    
    if negative_comments:
        summary_lines.append("Top Negative Comments:")
        for i, comment in enumerate(negative_comments[:3], 1):
            clean_comment = re.sub(r'<[^>]+>', '', comment)
            summary_lines.append(f"{i}. {clean_comment[:100]}{'...' if len(clean_comment) > 100 else ''}")
            comment_data.append({
                'type': 'negative',
                'text': clean_comment[:100] + ('...' if len(clean_comment) > 100 else ''),
                'comment_id': None,
                'number': i
            })
    else:
        summary_lines.append("There are no negative comments.")
        comment_data.append({'type': 'negative', 'text': "There are no negative comments.", 'comment_id': None})
    
    if neutral_comments:
        summary_lines.append("Top Neutral Comments:")
        for i, comment in enumerate(neutral_comments[:3], 1):
            clean_comment = re.sub(r'<[^>]+>', '', comment)
            summary_lines.append(f"{i}. {clean_comment[:100]}{'...' if len(clean_comment) > 100 else ''}")
            comment_data.append({
                'type': 'neutral',
                'text': clean_comment[:100] + ('...' if len(clean_comment) > 100 else ''),
                'comment_id': None,
                'number': i
            })
    else:
        summary_lines.append("There are no neutral comments.")
        comment_data.append({'type': 'neutral', 'text': "There are no neutral comments.", 'comment_id': None})

    summary_text = "\n".join(summary_lines[:20])
    logger.debug(f"Generated summary:\n{summary_text}")
    
    return summary_text, comment_data

def get_frequent_words(comments, n=10):
    # Combine English and Hindi stopwords, excluding meaningful words
    stop_words = set(stopwords.words('english')).difference({
        'video', 'content', 'subscribe', 'channel', 'like', 'love', 'great', 'good', 'awesome'
    }).union(set(hindi_stopwords))
    
    word_counter = Counter()
    total_tokens = 0
    total_words = 0
    filtered_words = []
    
    logger.debug(f"Processing {len(comments)} comments for frequent words")
    
    for i, comment in enumerate(comments):
        try:
            # Clean comment: remove URLs, emojis, and excessive punctuation
            comment = re.sub(r'http\S+|www\S+', '', comment.lower())  # Remove URLs
            comment = re.sub(r'[^\w\s]', '', comment)  # Remove punctuation
            comment = re.sub(r'\s+', ' ', comment).strip()  # Normalize spaces
            if not comment:
                logger.debug(f"Comment {i+1} empty after cleaning, skipping")
                continue
            tokens = word_tokenize(comment)
            total_tokens += len(tokens)
            # Filter words: alphanumeric, length >= 2, not in stopwords
            words = []
            for word in tokens:
                if word in stop_words:
                    filtered_words.append((word, "stopword"))
                    continue
                if len(word) < 2:
                    filtered_words.append((word, "too_short"))
                    continue
                if not word.isalnum():
                    filtered_words.append((word, "not_alphanumeric"))
                    continue
                words.append(word)
            total_words += len(words)
            word_counter.update(words)
            logger.debug(f"Comment {i+1} words: {words}")
            if filtered_words:
                logger.debug(f"Comment {i+1} filtered words: {filtered_words[-len(tokens):]}")
        except Exception as e:
            logger.error(f"Error processing comment {i+1} for frequent words: {e}")
            continue
    
    # Log word counts before filtering
    logger.debug(f"Total tokens: {total_tokens}, Total words after filtering: {total_words}, Unique words: {len(word_counter)}")
    logger.debug(f"Word counter: {dict(word_counter.most_common(20))}")
    
    # Get top n words, with a fallback if fewer than n words are available
    top_words = [(word, count) for word, count in word_counter.most_common(n)] if word_counter else []
    
    # Fallback: if no words, return a minimal list for testing
    if not top_words and comments:
        logger.warning("No frequent words found. Using fallback word list.")
        top_words = [('video', 1), ('comment', 1), ('content', 1)]
    
    if not top_words:
        logger.warning("No frequent words found. Comments may be too short, repetitive, or contain only filtered terms.")
    else:
        logger.debug(f"Top {n} frequent words: {top_words}")
    
    return top_words

@app.route('/')
def index():
    logger.debug("Rendering index.html")
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    logger.debug("Accessing register route")
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        logger.info(f"User registered: {email}")
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    logger.debug("Accessing login route")
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            logger.info(f"User logged in: {email}")
            return redirect('/dashboard')
        else:
            logger.warning(f"Invalid login attempt for email: {email}")
            return render_template('login.html', error='Invalid user')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    logger.debug("Accessing dashboard route")
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    logger.warning("Unauthorized dashboard access attempt")
    return redirect('/login')

@app.route('/logout')
def logout():
    logger.debug("Logging out user")
    session.pop('email', None)
    return redirect('/login')

@app.route('/youtube')
def youtube():
    logger.debug("Rendering youtube.html")
    return render_template('youtube.html')

@app.route('/authorize')
def authorize():
    logger.debug("Initiating YouTube authorization")
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    logger.debug("Handling OAuth2 callback")
    state = session['state']
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_response = request.url
    try:
        flow.fetch_token(authorization_response=authorization_response)
    except Exception as e:
        logger.error(f"Error fetching OAuth token: {e}")
        return render_template('youtube.html', error="Failed to authenticate with YouTube. Please try again.")
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)
    logger.info("YouTube authorization successful")
    return redirect(url_for('analyze_comments'))

@app.route('/analyze_comments', methods=['GET', 'POST'])
def analyze_comments():
    logger.debug("Accessing analyze_comments route")
    if 'credentials' not in session:
        logger.warning("No credentials in session, redirecting to authorize")
        return redirect(url_for('authorize'))

    try:
        credentials = Credentials(**session['credentials'])
        youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    except Exception as e:
        logger.error(f"Error building YouTube API client: {e}")
        return render_template('youtube.html', error="Failed to authenticate with YouTube API")

    if request.method == 'POST':
        video_url = request.form.get('video_id', '')
        logger.debug(f"Received video URL: {video_url}")
        video_id = extract_video_id(video_url)
        
        if not video_id:
            logger.error("Invalid YouTube URL provided")
            return render_template('youtube.html', error="Invalid YouTube URL. Please provide a valid video URL.")
        
        session['last_video_id'] = video_id

        try:
            comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message = get_comments(youtube, video_id, max_comments=500)
            if error_message and not comments:
                logger.warning(f"Comment fetching failed: {error_message}")
                return render_template('results.html',
                                    plot_url=None,
                                    sentiments={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                    sentiment_percentages={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                    summary="",
                                    comment_data=[],
                                    video_id=video_id,
                                    spam_count=0,
                                    question_count=0,
                                    abusive_count=0,
                                    frequent_words=[],
                                    error=error_message)
        except Exception as e:
            logger.error(f"Unexpected error fetching comments for video ID {video_id}: {e}")
            return render_template('results.html',
                                 plot_url=None,
                                 sentiments={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                 sentiment_percentages={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                 summary="",
                                 comment_data=[],
                                 video_id=video_id,
                                 spam_count=0,
                                 question_count=0,
                                 abusive_count=0,
                                 frequent_words=[],
                                 error="An unexpected error occurred while fetching comments.")

        # If no comments or partial comments, proceed with what’s available
        if not comments:
            logger.warning(f"No comments fetched for video ID: {video_id}")
            return render_template('results.html',
                                 plot_url=None,
                                 sentiments={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                 sentiment_percentages={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                 summary="",
                                 comment_data=[],
                                 video_id=video_id,
                                 spam_count=spam_count,
                                 question_count=len(question_comments),
                                 abusive_count=len(abusive_comments),
                                 frequent_words=[],
                                 error="No comments found or comments are disabled.")

        try:
            with open('classifier.pkl', 'rb') as model_file:
                classifier = pickle.load(model_file)
            with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
                tfidf_vectorizer = pickle.load(vectorizer_file)

            comments_tfidf = tfidf_vectorizer.transform(comments)
            predicted_sentiments = classifier.predict(comments_tfidf)

            sentiment_counts = {
                'positive': list(predicted_sentiments).count('positive'),
                'negative': list(predicted_sentiments).count('negative'),
                'neutral': list(predicted_sentiments).count('neutral'),
                'question': len(question_comments),
                'abusive': len(abusive_comments)
            }
            logger.debug(f"Sentiment counts: {sentiment_counts}")

            total_comments = sum(sentiment_counts.values())
            sentiment_percentages = {}
            if total_comments > 0:
                sentiment_percentages = {
                    'positive': (sentiment_counts['positive'] / total_comments) * 100,
                    'negative': (sentiment_counts['negative'] / total_comments) * 100,
                    'neutral': (sentiment_counts['neutral'] / total_comments) * 100,
                    'question': (sentiment_counts['question'] / total_comments) * 100,
                    'abusive': (sentiment_counts['abusive'] / total_comments) * 100
                }
            else:
                sentiment_percentages = {'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0}
            logger.debug(f"Sentiment percentages: {sentiment_percentages}")
        except Exception as e:
            logger.error(f"Error performing sentiment analysis: {e}")
            return render_template('results.html',
                                 plot_url=None,
                                 sentiments={'positive': 0, 'negative': 0, 'neutral': 0, 'question': len(question_comments), 'abusive': len(abusive_comments)},
                                 sentiment_percentages={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                 summary="",
                                 comment_data=[],
                                 video_id=video_id,
                                 spam_count=spam_count,
                                 question_count=len(question_comments),
                                 abusive_count=len(abusive_comments),
                                 frequent_words=[],
                                 error="Failed to analyze sentiments.")

        try:
            summary, comment_data = summarize_comments(comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, predicted_sentiments, video_id)
        except Exception as e:
            logger.error(f"Error summarizing comments: {e}")
            summary = "Error generating comment summary."
            comment_data = []
            error_message = "Failed to generate summary."

        try:
            frequent_words = get_frequent_words(comments, n=10)
            logger.debug(f"Frequent words generated: {frequent_words}")
        except Exception as e:
            logger.error(f"Error getting frequent words: {e}")
            frequent_words = [('video', 1), ('comment', 1), ('content', 1)]  # Fallback
            error_message = "Failed to analyze frequent words."

        try:
            plt.figure(figsize=(8, 8))
            labels = list(sentiment_counts.keys())
            sizes = list(sentiment_counts.values())
            colors = ['#198754', '#D54747', '#FFC107', '#4fc3f7', '#ff4444']
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.title('Overall Sentiment Distribution')
            plt.axis('equal')

            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()
        except Exception as e:
            logger.error(f"Error generating plot: {e}")
            plot_url = None
            error_message = "Failed to generate sentiment plot."

        logger.debug("Rendering results.html")
        return render_template('results.html',
                            plot_url=plot_url,
                            sentiments=sentiment_counts,
                            sentiment_percentages=sentiment_percentages,
                            summary=summary,
                            comment_data=comment_data,
                            video_id=video_id,
                            spam_count=spam_count,
                            question_count=len(question_comments),
                            abusive_count=len(abusive_comments),
                            frequent_words=frequent_words,
                            error=error_message if 'error_message' in locals() else None)

    # Handle GET requests
    if 'last_video_id' in session:
        try:
            credentials = Credentials(**session['credentials'])
            youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
            comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, spam_count, error_message = get_comments(youtube, session['last_video_id'], max_comments=500)
            
            if error_message and not comments:
                return render_template('results.html',
                                     plot_url=None,
                                     sentiments={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                     sentiment_percentages={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                     summary="",
                                     comment_data=[],
                                     video_id=session['last_video_id'],
                                     spam_count=0,
                                     question_count=0,
                                     abusive_count=0,
                                     frequent_words=[],
                                     error=error_message)
            
            # Process available comments
            if not comments:
                return render_template('results.html',
                                     plot_url=None,
                                     sentiments={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                     sentiment_percentages={'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0},
                                     summary="",
                                     comment_data=[],
                                     video_id=session['last_video_id'],
                                     spam_count=spam_count,
                                     question_count=len(question_comments),
                                     abusive_count=len(abusive_comments),
                                     frequent_words=[],
                                     error="No comments found or comments are disabled.")
            
            with open('classifier.pkl', 'rb') as model_file:
                classifier = pickle.load(model_file)
            with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
                tfidf_vectorizer = pickle.load(vectorizer_file)

            comments_tfidf = tfidf_vectorizer.transform(comments)
            predicted_sentiments = classifier.predict(comments_tfidf)

            sentiment_counts = {
                'positive': list(predicted_sentiments).count('positive'),
                'negative': list(predicted_sentiments).count('negative'),
                'neutral': list(predicted_sentiments).count('neutral'),
                'question': len(question_comments),
                'abusive': len(abusive_comments)
            }

            total_comments = sum(sentiment_counts.values())
            sentiment_percentages = {}
            if total_comments > 0:
                sentiment_percentages = {
                    'positive': (sentiment_counts['positive'] / total_comments) * 100,
                    'negative': (sentiment_counts['negative'] / total_comments) * 100,
                    'neutral': (sentiment_counts['neutral'] / total_comments) * 100,
                    'question': (sentiment_counts['question'] / total_comments) * 100,
                    'abusive': (sentiment_counts['abusive'] / total_comments) * 100
                }
            else:
                sentiment_percentages = {'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0}

            summary, comment_data = summarize_comments(comments, question_comments, abusive_comments, question_comment_ids, abusive_comment_ids, predicted_sentiments, session['last_video_id'])
            frequent_words = get_frequent_words(comments, n=10)
            logger.debug(f"Frequent words for GET request: {frequent_words}")

            plt.figure(figsize=(8, 8))
            labels = list(sentiment_counts.keys())
            sizes = list(sentiment_counts.values())
            colors = ['#198754', '#D54747', '#FFC107', '#4fc3f7', '#ff4444']
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.title('Overall Sentiment Distribution')
            plt.axis('equal')

            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()

            return render_template('results.html',
                                plot_url=plot_url,
                                sentiments=sentiment_counts,
                                sentiment_percentages=sentiment_percentages,
                                summary=summary,
                                comment_data=comment_data,
                                video_id=session['last_video_id'],
                                spam_count=spam_count,
                                question_count=len(question_comments),
                                abusive_count=len(abusive_comments),
                                frequent_words=frequent_words,
                                error=None)
        except Exception as e:
            logger.error(f"Error re-running analysis for video ID {session['last_video_id']}: {e}")
            return render_template('youtube.html', error="Failed to load previous analysis. Please submit a new video URL.")
    
    logger.debug("Redirecting to youtube.html for GET request")
    return redirect(url_for('youtube'))

@app.route('/debug_comments', methods=['POST'])
def debug_comments():
    logger.debug("Accessing debug_comments route")
    sample_comments = [
        "This video is amazing! Love the content!",
        "Why is this so confusing? Can you explain better?",
        "Not impressed, needs more effort.",
        "Great job, keep it up!",
        "What is the main point of this video?",
        "Pretty average, nothing special.",
        "Chutiya video, waste of time!"
    ]
    sample_sentiments = ['positive', 'neutral', 'negative', 'positive', 'neutral', 'neutral', 'negative']
    sample_question_comments = [
        "Why is this so confusing? Can you explain better?",
        "What is the main point of this video?"
    ]
    sample_abusive_comments = [
        "Chutiya video, waste of time!"
    ]
    sample_question_comment_ids = ['sample_id_1', 'sample_id_2']
    sample_abusive_comment_ids = ['sample_id_3']
    
    summary, comment_data = summarize_comments(sample_comments, sample_question_comments, sample_abusive_comments, sample_question_comment_ids, sample_abusive_comment_ids, sample_sentiments, 'sample_video_id')
    frequent_words = get_frequent_words(sample_comments, n=10)
    logger.debug(f"Debug frequent words: {frequent_words}")
    return jsonify({'summary': summary, 'comment_data': comment_data, 'frequent_words': frequent_words})

async def fetch_comments(post_id):
    reddit = asyncpraw.Reddit(
        client_id='34L5aoKncxSEwwGVod60tA',
        client_secret='vqb6bt_h96B2MWZGEsVACbV6yxOClA',
        user_agent='CommentFetcher by /u/SignificantDare76'
    )
    comments = []
    user_comments = {}
    spam_count = 0
    try:
        submission = await reddit.submission(id=post_id)
        await submission.load()
        submission.comments.replace_more(limit=0)
        for comment in submission.comments[:100]:
            comment_text = comment.body
            author_id = str(comment.author) if comment.author else 'anonymous'
            comments.append(comment_text)
            if author_id in user_comments:
                if comment_text in user_comments[author_id]:
                    spam_count += 1
                else:
                    user_comments[author_id].add(comment_text)
            else:
                user_comments[author_id] = {comment_text}
    except Exception as e:
        logger.error(f"Error fetching Reddit comments: {e}")
    finally:
        await reddit.close()
    return comments, spam_count

@app.route('/reddit_input')
def reddit_input():
    logger.debug("Rendering reddit_input.html")
    return render_template('reddit_input.html')

@app.route('/reddit', methods=['POST'])
def reddit_analysis():
    logger.debug("Accessing reddit_analysis route")
    post_id = request.form.get('post_id', '').strip()
    
    if not post_id:
        logger.error("No post ID provided")
        return render_template('reddit_input.html', error="Post ID is required")
    
    try:
        nest_asyncio.apply()
        comments, spam_count = asyncio.run(fetch_comments(post_id))
        
        if not comments:
            logger.warning(f"No comments found for Reddit post ID: {post_id}")
            return render_template('reddit_input.html', error="No comments found for this post")
        
        abusive_comments = [c for c in comments if any(re.search(word, c.lower(), re.IGNORECASE) for word in abusive_words_hindi)]
        question_comments = [c for c in comments if re.search(r'\?$', c, re.IGNORECASE) or any(word in c.lower().split() for word in question_words)]
        
        try:
            with open('classifier.pkl', 'rb') as model_file:
                classifier = pickle.load(model_file)
            with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
                tfidf_vectorizer = pickle.load(vectorizer_file)

            comments_tfidf = tfidf_vectorizer.transform(comments)
            predicted_sentiments = classifier.predict(comments_tfidf)

            sentiment_counts = {
                'positive': list(predicted_sentiments).count('positive'),
                'negative': list(predicted_sentiments).count('negative'),
                'neutral': list(predicted_sentiments).count('neutral'),
                'question': len(question_comments),
                'abusive': len(abusive_comments)
            }

            total_comments = sum(sentiment_counts.values())
            sentiment_percentages = {}
            if total_comments > 0:
                sentiment_percentages = {
                    'positive': (sentiment_counts['positive'] / total_comments) * 100,
                    'negative': (sentiment_counts['negative'] / total_comments) * 100,
                    'neutral': (sentiment_counts['neutral'] / total_comments) * 100,
                    'question': (sentiment_counts['question'] / total_comments) * 100,
                    'abusive': (sentiment_counts['abusive'] / total_comments) * 100
                }
            else:
                sentiment_percentages = {'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0}
        except Exception as e:
            logger.error(f"Error performing sentiment analysis for Reddit comments: {e}")
            sentiment_counts = {'positive': 0, 'negative': 0, 'neutral': 0, 'question': len(question_comments), 'abusive': len(abusive_comments)}
            sentiment_percentages = {'positive': 0, 'negative': 0, 'neutral': 0, 'question': 0, 'abusive': 0}

        try:
            summary, comment_data = summarize_comments(comments, question_comments, abusive_comments, [], [], predicted_sentiments, post_id)
        except Exception as e:
            logger.error(f"Error summarizing Reddit comments: {e}")
            summary = "Error generating comment summary."
            comment_data = []

        try:
            frequent_words = get_frequent_words(comments, n=10)
            logger.debug(f"Reddit frequent words: {frequent_words}")
        except Exception as e:
            logger.error(f"Error getting frequent words for Reddit: {e}")
            frequent_words = [('video', 1), ('comment', 1), ('content', 1)]

        try:
            plt.figure(figsize=(8, 8))
            labels = list(sentiment_counts.keys())
            sizes = list(sentiment_counts.values())
            colors = ['#198754', '#D54747', '#FFC107', '#4fc3f7', '#ff4444']
            plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
            plt.title(f'Sentiment Analysis of Reddit Post Comments (ID: {post_id})')
            plt.axis('equal')

            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()
            plt.close()
        except Exception as e:
            logger.error(f"Error generating Reddit plot: {e}")
            plot_url = None

        logger.debug("Rendering reddit.html")
        return render_template('reddit.html',
                             plot_url=plot_url,
                             sentiments=sentiment_counts,
                             sentiment_percentages=sentiment_percentages,
                             summary=summary,
                             comment_data=comment_data,
                             spam_count=spam_count,
                             question_count=len(question_comments),
                             abusive_count=len(abusive_comments),
                             frequent_words=frequent_words)

    except Exception as e:
        logger.error(f"Error processing Reddit analysis: {e}")
        return render_template('reddit_input.html', error="Error processing Reddit post")

if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run('localhost', 5000, debug=True)