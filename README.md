<h1 align="center" style="font-size: 40px;">🎉 CommentLens 🌟</h1>

<h2 align="center">Transforming Feedback into Action with AI for Good</h2>







  
<h3 style = "font-size: 20px;"> What is CommentLens?</h3>

CommentLens is a AI-powered web app that turns messy YouTube and Reddit comments into easy insights, helping 1 million+ creators, 50 million+ users, and businesses find good feedback, remove rude comments, and reply quickly, managing 1.8 lakhs (180,000) comments daily













<h3 style = "font-size: 20px;"> Motivation</h3>

The inspiration for CommentLens stems from the growing frustration we’ve seen among creators, moderators, and businesses struggling to navigate the wild world of social media comments. With 500 hours of video uploaded to YouTube hourly and 1.2 billion Reddit comments yearly, we noticed how toxic remarks, spam, and buried feedback were hurting online communities and mental well-being, especially with hurtful Hindi words often ignored. Motivated by the need to create safer, smarter digital spaces, we aimed to empower the 1 million+ YouTubers, 50 million+ Reddit users, and countless brands with a tool that saves time and builds trust. Our passion for AI and a desire to solve real-world problems drove us to develop CommentLens, turning a personal mission into a solution that makes online interaction better for everyone.





<h3 style = "font-size: 20px;">Features</h3>


**1. Real-Time Analysis:** Sorts comments into categories with 85%+ accuracy using 1.8 lakhs daily YouTube API limit.  

**2. Hindi Toxicity Detection:** Spots Hindi abusive words with 95% precision.

**3. Toxic Comment Deletion:** Removes toxic comments directly from the site.

**4. Instant Replies:** Answers question comments instantly.

**5. Topic Highlights:** Extracts key nouns (e.g., "product: 15") with NLTK.

**6. Smart Summaries:** Summarizes top comments with LexRank.

**7. Visual Insights:** Shows pie charts and progress bars via Matplotlib.

**8. Spam Flagging:** Flags spam comments efficiently.

**9. User-Friendly UI:** Offers a dark-themed, animated interface with Bootstrap/CSS.

**10. Secure Data:** Stores user data securely with Flask-SQLAlchemy and bcrypt.

**11. Fast Processing:** Handles 1K comments in under 10 seconds.

























<h3 style = "font-size: 20px;">Tech Stack</h3>


1. Languages: Python 3.8+
2. Frameworks: Flask (web framework), SQLAlchemy (database ORM)
3. Libraries:
   • google-api-python-client: For YouTube Data API integration
   
   • nltk: For sentiment analysis and topic extraction
   
   • sumy: For comment summarization
   
   • matplotlib: For generating pie charts
   
   • bcrypt: For secure password hashing
   
   • omnidimension: For voice-based insights
5. Frontend: Bootstrap 5 (via CDN), HTML, CSS, JavaScript
6. Database: SQLite
7. APIs: YouTube Data API v3 nad Reddit API
8. Models: Pre-trained classifier.pkl and tfidf_vectorizer.pkl for sentiment analysis











<h3 style = "font-size: 20px;">Installation</h3>

 
Let’s get CommentLens running on your system (Windows, macOS, or Linux) with these simple steps!



<h4 >Step 1: Clone the Repository</h4>

Grab the CommentLens code from GitHub.

  Clone Repository
  
    git clone https://github.com/TarunGoel93/CommentLens.git
    
    cd CommentLens
  


Replace TarunGoel93 with your GitHub username if you’ve forked the repository.


<h4>Step 2: Set Up a Virtual Environment</h4>

Create a virtual environment to keep dependencies organized.

  Set Up Virtual Environment
  
    # Create virtual environment
    
    python -m venv venv

    Activate virtual environment On Windows venv\Scripts\activate On macOS/Linux source venv/bin/activate  


<h4>Step 3: Install Dependencies</h4>

Install the required Python packages. If requirements.txt isn’t included, create it with this content.

  Create requirements.txt
  
    flask==2.0.1
    
    sqlalchemy==1.4.39
    
    bcrypt==4.0.1
    
    google-api-python-client==2.64.0
    
    nltk==3.7
    
    matplotlib==3.5.3
    
    sumy==0.11.0
    
    requests==2.28.1
    
    omnidimension==0.1.0  
  


Then install the packages:

  Install Dependencies
  
    pip install -r requirements.txt
  


<h4>Step 4: Download NLTK Data</h4>
CommentLens uses NLTK for text processing. Download the necessary data.

  Download NLTK Data
  
    python -m nltk.downloader punkt stopwords
  


<h4>Step 5: Install Bootstrap (Optional)</h4>
CommentLens uses Bootstrap 5 via CDN. To host it locally for customization:

  Install Bootstrap via npm
  
    npm install bootstrap@5.3.7
  


Copy node_modules/bootstrap/dist/ to your static/ folder and update templates (e.g., dashboard.html) to use local files instead of:

  Bootstrap CDN Links
  
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-7qAoOXltbVP82dhxHAUje59V5r2YsVfBafyUDxEdApLPmcdhBPg1DKg1ERo0BZlK" crossorigin="anonymous">
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>

  








<h3 style = "font-size: 20px;">Configuration</h3>




<h4>Step 6: Set Up YouTube API</h4>

1. Go to the Google Cloud Console.
2. Create a project and enable the YouTube Data API v3.
3. Download credentials as client_secret.json.
4. Place client_secret.json in the project root.


  Place YouTube API Credentials
  
    mv /path/to/client_secret.json CommentLens/client_secret.json




  
<h4>Step 7: Set Up Reddit API</h4>

1. Go to Reddit Apps and create a new application.

2. Note the client_id and client_secret.

3. Update the Reddit API credentials in app.py:


  Place Reddit API Credentials
  
    # In app.py, update the asyncpraw.Reddit call
    
    reddit = asyncpraw.Reddit(
    
    client_id='your_client_id',
    
    client_secret='your_client_secret',
    
    user_agent='CommentLens by /u/your_reddit_username'
    
    )


<h4>Step 7: Set Up Omnidimension API</h4>

The voice insights feature uses the Omnidimension API. Update the API key and details in app.py.

  Update Omnidimension API Key
  
    # In app.py, update the /initiate_call route
    
    api_key = "your_omnidimension_api_key"
    
    client = Client(api_key)
    
    agent_id = your_agent_id  # Obtain from Omnidimension dashboard
     
    to_number = "your_support_number"  # E.164 format, e.g., +1234567890
  


Note: If omnidimension is a placeholder, use Twilio instead:

  Install Twilio (Alternative)
  
    pip install twilio
  



  Update Twilio Code in app.py
  
    from twilio.rest import Client as TwilioClient

    @app.route('/initiate_call', methods=['POST'])def initiate_call():    if 'email' not in session:        return jsonify({'success': False, 'error': 'You must be logged in to initiate a call'}), 401    try:        client = TwilioClient("your_account_sid", "your_auth_token")        call = client.calls.create(            to="+919210034977",            from_="your_twilio_number",            url="http://demo.twilio.com/docs/voice.xml"        )        logger.info(f"Call initiated: {call.sid}")        return jsonify({'success': True, 'message': 'Call initiated successfully'})    except Exception as e:        logger.error(f"Error initiating call: {e}")        return jsonify({'success': False, 'error': str(e)}), 500  


<h4>Step 8: Initialize the Database</h4>

Set up the SQLite database for user authentication.

  Initialize SQLite Database
  
    python
    
    from app import app, db
    
    with app.app_context():
    
    db.create_all()
    
    exit()
  






<h3 style = "font-size: 20px;">Usage</h3>

<h4>Step 9: Run the Application</h4>

Start the Flask server to launch CommentLens.

  Run Flask Application
  
    python app.py
  


Open your browser and visit http://localhost:5000.



<h4>Step 10: Explore CommentLens</h4>

Register/Login: Sign up or log in at http://localhost:5000/login.

Analyze Comments:

Go to http://localhost:5000/youtube.

Authenticate with Google and enter a YouTube video URL (e.g., https://www.youtube.com/watch?v=VIDEO_ID).

View sentiment analysis, topic extraction, and a pie chart.


Voice Insights:

From the dashboard (http://localhost:5000/dashboard), click “Get Voice Insights” to receive a call with a summary of comment insights.



Example Command (to test voice insights via API):

  Test Voice Insights
  
    curl -X POST http://localhost:5000/initiate_call -H "Content-Type: application/json"
  





🤝 Contributing
We’d love your help to make CommentLens even better! To contribute:

Fork the repository.


Create a feature branch: git checkout -b feature/your-feature.



Commit your changes: git commit -m "Add your feature".



Push to the branch: git push origin feature/your-feature.




Open a pull request.


Developer: Tarun Goel (@TarunGoel93).
Libraries: Thanks to nltk, sumy, matplotlib, Flask, and google-api-python-client.
Tools: Powered by Python, SQLite, and Bootstrap 5.
# CommentLens
