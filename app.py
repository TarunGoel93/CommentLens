from flask import Flask, redirect, url_for, session, request, render_template
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
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

    def _init_(self, email, password, name):
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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        new_user = User(name=name, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['email'] = user.email
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid user')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')

@app.route('/youtube')
def youtube():
    return render_template('youtube.html')

@app.route('/authorize')
def authorize():
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_url, state = flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)

@app.route('/oauth2callback')
def oauth2callback():
    state = session['state']
    flow = Flow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)
    flow.redirect_uri = url_for('oauth2callback', _external=True)
    authorization_response = request.url
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)
    return redirect(url_for('analyze_comments'))

def get_comments(youtube, video_id):
    comments = []
    user_comments = {}
    spam_count = 0

    request = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100
    )
    response = request.execute()

    for item in response.get('items', []):
        comment_text = item['snippet']['topLevelComment']['snippet']['textDisplay']
        author_id = item['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
        
        comments.append(comment_text)
        
        if author_id in user_comments:
            if comment_text in user_comments[author_id]:
                spam_count += 1
            else:
                user_comments[author_id].add(comment_text)
        else:
            user_comments[author_id] = {comment_text}

    return comments, spam_count

def summarize_comments(comments, sentiments):
    positive_comments = [c for c, s in zip(comments, sentiments) if s == 'positive']
    negative_comments = [c for c, s in zip(comments, sentiments) if s == 'negative']
    
    summary_lines = []
    
    if positive_comments:
        summary_lines.append("Top Positive Comments:")
        for i, comment in enumerate(positive_comments[:2], 1):
            summary_lines.append(f"{i}. {comment[:100]}{'...' if len(comment) > 100 else ''}")
    
    if negative_comments:
        if summary_lines:
            summary_lines.append("")
        summary_lines.append("Top Negative Comments:")
        for i, comment in enumerate(negative_comments[:2], 1):
            summary_lines.append(f"{i}. {comment[:100]}{'...' if len(comment) > 100 else ''}")
    
    if len(summary_lines) < 7 and comments:
        if summary_lines:
            summary_lines.append("")
        text = " ".join(comments[:3])
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, 2)
        summary_lines.append("Summary:")
        for sentence in summary:
            summary_lines.append(str(sentence))
    
    return "\n".join(summary_lines[:8])

@app.route('/analyze_comments', methods=['GET', 'POST'])
def analyze_comments():
    if 'credentials' not in session:
        return redirect(url_for('authorize'))

    credentials = Credentials(**session['credentials'])
    youtube = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    if request.method == 'POST':
        video_id = request.form['video_id']
        comments, spam_count = get_comments(youtube, video_id)
        
        with open('classifier.pkl', 'rb') as model_file:
            classifier = pickle.load(model_file)
        with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
            tfidf_vectorizer = pickle.load(vectorizer_file)

        comments_tfidf = tfidf_vectorizer.transform(comments)
        predicted_sentiments = classifier.predict(comments_tfidf)

        sentiment_counts = {
            'positive': list(predicted_sentiments).count('positive'),
            'negative': list(predicted_sentiments).count('negative'),
            'neutral': list(predicted_sentiments).count('neutral')
        }

        summary = summarize_comments(comments, predicted_sentiments)

        plt.figure(figsize=(10, 6))
        plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), 
               autopct='%1.1f%%', colors=['#198754', '#D54747', '#FFC107'])
        plt.title('Sentiment Analysis of YouTube Comments')
        plt.tight_layout()

        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('results.html', 
                            plot_url=plot_url, 
                            sentiments=sentiment_counts, 
                            summary=summary, 
                            spam_count=spam_count)

    return render_template('youtube.html')

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
        print(f"Error fetching Reddit comments: {e}")
    finally:
        await reddit.close()
    return comments, spam_count


@app.route('/reddit_input')
def reddit_input():
    return render_template('reddit_input.html')

@app.route('/reddit', methods=['POST'])
def reddit_analysis():
    post_id = request.form.get('post_id', '').strip()
    
    if not post_id:
        return render_template('reddit_input.html', error="Post ID is required")
    
    try:
        nest_asyncio.apply()
        comments, spam_count = asyncio.run(fetch_comments(post_id))
        
        if not comments:
            return render_template('reddit_input.html', error="No comments found for this post")
        
        with open('classifier.pkl', 'rb') as model_file:
            classifier = pickle.load(model_file)
        with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:
            tfidf_vectorizer = pickle.load(vectorizer_file)

        comments_tfidf = tfidf_vectorizer.transform(comments)
        predicted_sentiments = classifier.predict(comments_tfidf)

        sentiment_counts = {
            'positive': list(predicted_sentiments).count('positive'),
            'negative': list(predicted_sentiments).count('negative'),
            'neutral': list(predicted_sentiments).count('neutral')
        }

        summary = summarize_comments(comments, predicted_sentiments)

        plt.figure(figsize=(10, 6))
        plt.pie(sentiment_counts.values(), labels=sentiment_counts.keys(), 
               autopct='%1.1f%%', colors=['#198754', '#D54747', '#FFC107'])
        plt.title(f'Sentiment Analysis of Reddit Post Comments (ID: {post_id})')
        plt.tight_layout()

        img = BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()

        return render_template('reddit.html', 
                             plot_url=plot_url, 
                             sentiments=sentiment_counts, 
                             summary=summary, 
                             spam_count=spam_count)
    
    except Exception as e:
        print(f"Error processing Reddit analysis: {e}")
        return render_template('reddit_input.html', error="Error processing Reddit post")

# ... (keep all other existing routes and functions)

if __name__ == '_main_':
    app.run('localhost', 5000, debug=True)

if __name__ == '_main_':
    app.run('localhost', 5000, debug=True)