🎉 CommentLens 🌟


CommentLens is a super cool web app that helps YouTubers and Redditors understand their comments! 😄 It checks your comments, finds what fans love, spots questions, and catches rude stuff—all with fun charts and easy tips. It’s like a magic wand for your comment section! 🪄

__________________________________________________________________________________________________________________________________________________________________________________

😩 Why Comments Are Hard
If you make YouTube videos or Reddit posts, you get TONS of comments! Some say “This rocks!” 😍, others ask “What’s next?”, and a few might be mean 😣. But here’s the problem:

Too Many! Reading thousands takes forever. ⏳
Rude Ones! Mean comments make fans sad. 😞
Missed Ideas! You might skip questions or tips for your next big hit. 💡

Going through comments by hand is super tough. You need a fun way to know what your fans are saying! 😊

🌈 How CommentLens Saves the Day

CommentLens is your comment superhero! 🦸‍♀️ It looks at up to 500 comments (100 for free) and shows you:


Fan Moods: Are they happy 😄, upset 😞, or chill 😐?
Questions: Finds “What’s this?” so you can answer.
Rude Alerts: Spots mean comments (even in Hindi!) to keep things nice.
Hot Words: Shows words like “funny” or “tutorial” to plan your next post.
Smart Tips (Coming Soon): Groq AI will give you quick summaries and ideas!

It saves time, makes fans happy, and helps your channel grow! 💖

🌟 Cool Things CommentLens Does



Feature
What It Does



🌍 Fast Grab
Gets YouTube or Reddit comments in a snap!


😎 Mood Sort
Labels comments as happy, sad, or neutral.


🛑 Rude Stopper
Catches mean comments to keep things friendly.


🔍 Word Finder
Spots popular words for new ideas.


📊 Fun Charts
Shows colorful charts of fan feelings.


🧠 AI Tips (Soon)
Groq AI will suggest video ideas!


🔐 Safe Login
Connects safely to get your comments.




🧰 What’s It Made Of?
CommentLens uses awesome tools to work its magic! 🌟

Python: Our coding superhero! 🐍
Flask: Makes the app fast and fun.
SQLite: Saves your account info safely.
YouTube & Reddit Tools: Grab comments like a pro.
Groq AI (Soon): Gives smart content tips.
Smart Readers: Guess comment moods with brainy tricks.
Charts: Draws pretty pictures of what fans feel.
Web Design: Makes everything look cool!


💫 Why You’ll Love It

CommentLens makes being a creator EASY!


Saves Time: No reading comments all day! ⏰
Happy Fans: Answer questions and keep things nice. 😊
Bigger Channel: Use fan ideas to make hits. 📈
Fun Vibes: Creates a friendly comment zone. 🎉

Whether you’re a new YouTuber or Reddit pro, CommentLens helps you shine! ✨

🚀 Try It Out!
Want to play with CommentLens? It’s easy to set up on your computer! 🖥️
What You Need

Python 3.8 or newer.
Git to grab our code.
YouTube and Reddit keys (get from Google/Reddit).
Two files: classifier.pkl and tfidf_vectorizer.pkl (ask us!).

Steps to Start

Get the Code:
git clone https://github.com/TarunGoel93/CommentLens.git
cd CommentLens


Make a Safe Space:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate


Add Fun Tools:
pip install flask flask-sqlalchemy bcrypt google-auth-oauthlib google-api-python-client sumy asyncpraw nltk matplotlib scikit-learn requests python-dotenv


Grab Extra Bits:
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"


Set Up Secrets:

Put client_secret.json (YouTube key) in the folder.
Make a .env file:REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
GROQ_API_KEY=your_key




Add Special Files:

Drop classifier.pkl and tfidf_vectorizer.pkl in the folder. (Email us for them!)


Blast Off:
python app.py

Open http://localhost:5000 in your browser and have fun! 🎉


How to Use

Sign up for an account.
Paste a YouTube video link or Reddit post ID.
See cool charts and comment insights!


📷 Sneak Peek



Dashboard
Results








Tip: Add real screenshots to /assets for extra sparkle! ✨


🎥 See It Live
Check out our demo video to see CommentLens rock! (Add your video link here.) 🎬

🌟 What’s Coming Next?
We’re making CommentLens even cooler! Soon:

AI tips to summarize comments and suggest videos.
Find out if fans are excited or curious.
Live comment alerts.
Fancy charts like word clouds.
Support for more languages.


🤗 Help Us Grow

Love CommentLens? Add your magic! 🎈


Copy our code (fork on GitHub).
Add a feature: git checkout -b my-cool-idea.
Save it: git commit -m "Added cool idea".
Share: git push origin my-cool-idea.
Tell us: Open a Pull Request.

Check our Code of Conduct and report bugs here.

📜 Free to Use
CommentLens is free for everyone under the MIT License. Play with it, share it, make it yours! 😄

👨‍🚀 Our Team

Tarun Goel: Code Wizard & Comment Tamer
Add your friends here!


💬 Say Hi!
Got ideas or questions? Reach out:

GitHub: TarunGoel93
Email: your.email@example.com
Issues: GitHub Issues



Made with 💕 for creators everywhere! Let’s make comments FUN! 🌈

