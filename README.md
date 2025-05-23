
  CommentLens 🌈
  Your AI-Powered Sidekick for Smashing Comment Chaos! 🚀




🎉 What is CommentLens?
CommentLens is the ultimate AI-powered web platform that turns YouTube and Reddit comment chaos into pure gold! 💎 Built for content creators, social media gurus, and community managers, it uses machine learning and natural language processing to analyze comments, uncover sentiments, zap toxic remarks, and deliver actionable insights. Whether you’re a YouTuber craving feedback or a Redditor seeking trends, CommentLens saves time, boosts engagement, and keeps your community vibe positive! 😎


💥 The Problem We Solve
Imagine drowning in thousands of YouTube or Reddit comments—praise, rants, questions, and the occasional toxic jab. 😩 Manually sorting this mess is a nightmare, leading to:

Missed Vibes: You skip audience questions or overlook what fans love.
Toxic Overload: Abusive comments sour your community and brand.
Content Guesswork: Without insights, your next video or post might flop.

Creators need a way to cut through the noise, spot trends, and keep things chill—fast.

🌟 Our Solution: CommentLens
CommentLens is your superhero sidekick, wielding AI and ML to analyze up to 2k comments per video or post. 🦸‍♂️ It delivers:

Sentiment Magic: Splits comments into positive, negative, neutral, question, or abusive buckets.
Toxicity Shield: Flags nasty comments (even Hindi slang!) for quick moderation.
Spam Zapper: Catches repetitive or spammy comments to keep things clean.
Trend Spotter: Highlights frequent words to inspire your next hit content.
AI Insights (Coming Soon): Groq-powered summaries and recommendations to level up your strategy.

With a free tier (100 comments) and a paid tier (500 comments), CommentLens is built for creators big and small. Turn comment chaos into a roadmap for growth! 🚀

  See It in Action! 🎥
  Check out our demo video to watch CommentLens crush comment analysis!



🔥 Key Features

⚡ Real-Time Analysis: Grabs YouTube/Reddit comments in a flash via APIs.
😊 Sentiment Breakdown: Uses ML to tag comments with pinpoint accuracy.
🛡️ Multilingual Toxicity Detection: Spots abusive comments, including Hindi slang, with regex magic.
📊 Slick Dashboard: Shows sentiment pie charts, frequent words, and key comments with moderation links.
🔒 Secure OAuth: Connects safely to YouTube accounts for comment access.
🧠 AI Summaries (Planned): Groq API will deliver snappy summaries and content tips.
📈 Scalable Tiers: Free (100 comments) or paid (500 comments) to fit your needs.



🛠️ Tech Stack
CommentLens rocks a vibrant, modern tech stack that’s as powerful as it is colorful! 🌈
Backend

Python 3.8+: The heart of our ML and web magic.
Flask: Lightweight framework for snappy APIs and routes.
SQLAlchemy + SQLite: Stores user data with ORM ease.
Google YouTube Data API v3: Fetches YouTube comments with OAuth 2.0.
asyncpraw: Grabs Reddit comments asynchronously.
Groq API (llama3-8b-8192) (Planned): Powers AI-driven insights.

Machine Learning & NLP

scikit-learn: Drives sentiment analysis with TF-IDF and a trained classifier.
NLTK: Cleans text with tokenization and stopword removal (English/Hindi).
sumy: Crafts summaries with LexRank for comment highlights.
transformers (Future): For emotion clustering or advanced toxicity detection.

Frontend

HTML/CSS + Jinja2: Builds a bold, responsive UI with sentiment visuals.
Matplotlib: Paints colorful pie charts for sentiment distribution.

Security & Tools

bcrypt: Locks down passwords with secure hashing.
python-dotenv (Recommended): Keeps API keys safe in .env.
Logging: Tracks API calls and errors like a pro.
Git: Powers version control for team awesomeness.


🌍 Why CommentLens Rocks
CommentLens isn’t just a tool—it’s a game-changer for creators:

⏰ Saves Hours: Automates comment analysis, letting you focus on creating.
💬 Boosts Engagement: Spots questions and trends to spark audience love.
🛡️ Cleans Communities: Zaps toxic comments for a positive vibe.
📈 Fuels Growth: Turns feedback into strategies for viral content.

Whether you’re a solo YouTuber or a Reddit mod, CommentLens helps you shine! ✨

🚀 Get Started
Ready to unleash CommentLens? Here’s how to set it up locally:
Prerequisites

Python 3.8+
Git
YouTube API credentials (client_secret.json from Google Cloud Console)
Reddit API credentials (client ID, secret)
ML models (classifier.pkl, tfidf_vectorizer.pkl)

Installation

Clone the Repo:
git clone https://github.com/TarunGoel93/CommentLens.git
cd CommentLens


Set Up Virtual Environment:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Install Dependencies:
pip install flask flask-sqlalchemy bcrypt google-auth-oauthlib google-api-python-client sumy asyncpraw nltk matplotlib scikit-learn requests python-dotenv


Download NLTK Data:
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"


Configure API Keys:

Add client_secret.json to the project root for YouTube API.
Create .env:REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
GROQ_API_KEY=your_groq_api_key




Add ML Models:

Place classifier.pkl and tfidf_vectorizer.pkl in the root. (Ping us for models or train your own!)


Run It:
python app.py

Hit http://localhost:5000 and start analyzing! 🚀


Usage

Sign Up/Login: Create an account to unlock the dashboard.
YouTube Analysis: Authenticate via OAuth, enter a video URL, and explore sentiments, key comments, and trends.
Reddit Analysis: Input a post ID at /reddit_input for similar insights.
Debug Mode: Test with sample data at /debug_comments.




🎥 Demo
Watch CommentLens in action! Demo Video (add your video link here).

🔮 What’s Next?
We’re pumped to make CommentLens even crazier! Future plans include:

Groq AI Integration: Snappy summaries and recommendations for key comments.
Emotion Vibes: Cluster comments by emotions (joy, anger) with transformers.
Live Alerts: Real-time comment monitoring with browser pings.
Fancy Visuals: Word clouds and Plotly charts for extra flair.
Global Reach: Support for more languages in toxicity detection.
Cloud Power: Deploy with PostgreSQL, Redis, and Docker.


🤝 Join the Party
Love CommentLens? Jump in and make it better! 🎉

Fork the repo.
Create a branch: git checkout -b feature/YourEpicFeature.
Commit: git commit -m "Add EpicFeature".
Push: git push origin feature/YourEpicFeature.
Open a Pull Request.

Check our Code of Conduct and file issues at GitHub Issues.

📜 License
CommentLens is open-source under the MIT License. Use, tweak, and share it freely! 🥳

👨‍💻 Team

Tarun Goel - Lead Developer & ML Wizard
Shubh Singhal


📬 Get in Touch
Got ideas or questions? Hit us up:

GitHub: TarunGoel93
Email: goeltarun15@gmail.com
Issues: GitHub Issues



  Built with 💖 for creators everywhere. Let’s make comments awesome! 🚀
