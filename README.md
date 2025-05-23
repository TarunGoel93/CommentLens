
  🎉 CommentLens 🎉
  Turn Your YouTube & Reddit Comments into Super Cool Insights! 🚀




🌈 What’s CommentLens?
Imagine you’re a YouTuber or Reddit star with TONS of comments on your videos or posts. Some are super sweet 😍, some are mean 😣, and others are questions like “What’s next?” Sorting through them is like finding a needle in a haystack! 😵
CommentLens is your new best friend! It’s a fun web app that looks at your comments and tells you what’s up in a snap. It spots happy vibes, grumpy ones, questions, and even rude comments, then shows you cool charts and tips to make your content AWESOME. It’s like having a superhero assistant for your comment section! 🦸‍♀️


😩 Why Do You Need It?
If you make videos or posts, you know comments are a BIG deal. But:

Too Many Comments: Reading thousands takes forever!
Rude Stuff: Mean comments can make your fans sad.
Missed Ideas: You might skip questions or cool feedback that could make your next video a hit.

Going through comments by hand is super hard and no fun. You need a way to understand your fans FAST and keep your community happy! 😊

🎨 How CommentLens Saves the Day
CommentLens is like a magic wand for your comments! 🪄 It checks up to 2k comments (100 for free users) and gives you:

Mood Check: Are fans happy 😄, upset 😞, or just chill 😐?
Question Finder: Spots questions like “What’s this about?” so you can answer them.
Rude Comment Alert: Finds mean comments (even in Hindi!) to keep your page nice.
Hot Words: Shows words fans use a lot, like “tutorial” or “funny,” to plan your next post.
Smart Tips (Coming Soon): Uses Groq AI to give you short summaries and ideas, like “Make a video about X!”

It’s easy to use, saves you tons of time, and makes your fans love you even more! 💖

  🎥 Watch the Magic!
  See CommentLens in action with our demo video! 🚀



🌟 Cool Things CommentLens Does

🌍 Grabs Comments Fast: Pulls comments from YouTube or Reddit in seconds.
😎 Sorts Moods: Labels comments as happy, sad, neutral, questions, or rude.
🛑 Stops Meanies: Finds rude comments so you can delete them.
🔍 Finds Trends: Shows popular words to spark your next big idea.
📊 Pretty Charts: Makes colorful pie charts to see what fans feel.
🔐 Safe Login: Connects to YouTube securely to grab comments.
🧠 Smart AI (Soon): Groq AI will summarize comments and give you pro tips!



🧰 What’s It Made Of?
CommentLens is built with fun, powerful tools that make it shine! 🌟 Here’s the scoop:

Python: Our coding superhero that runs everything! 🐍
Flask: A cool tool that makes our web app zippy and fun.
SQLite: A tiny database to save your account info safely.
YouTube API: Grabs comments from your videos like magic.
Reddit API: Snags comments from Reddit posts.
Groq AI (Coming Soon): A brainy AI to give you smart comment tips.
scikit-learn & NLTK: Fancy tools that read comments and guess their mood.
Matplotlib: Draws awesome charts to show what fans think.
HTML/CSS: Makes our app look pretty and easy to use.
bcrypt: Keeps your password super safe.

It’s like a candy store of tech, all mixed together to make CommentLens sweet! 🍬

💫 Why You’ll Love It
CommentLens is your ticket to a happier, easier creator life:

Saves Time: No more reading comments for hours!
Makes Fans Happy: Answer questions and delete rude stuff fast.
Grows Your Channel: Use fan feedback to make videos they LOVE.
Keeps It Chill: Creates a friendly, fun comment section.

Whether you’re a new YouTuber or a Reddit pro, CommentLens is here to make you a star! 🌟

🚀 Try It Out!
Want to test CommentLens? It’s super easy to set up on your computer! 🖥️
What You Need

A computer with Python 3.8 or newer.
Git to grab our code.
A YouTube API key (get one from Google’s website).
A Reddit API key (from Reddit’s developer site).
Two special files: classifier.pkl and tfidf_vectorizer.pkl (ask us for them!).

Steps to Start

Get the Code:
git clone https://github.com/TarunGoel93/CommentLens.git
cd CommentLens


Make a Safe Space:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Add Fun Tools:
pip install flask flask-sqlalchemy bcrypt google-auth-oauthlib google-api-python-client sumy asyncpraw nltk matplotlib scikit-learn requests python-dotenv


Grab Extra Bits:
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"


Set Up Secrets:

Put client_secret.json (YouTube key) in the CommentLens folder.
Make a .env file with:REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
GROQ_API_KEY=your_groq_api_key




Add Special Files:

Drop classifier.pkl and tfidf_vectorizer.pkl in the CommentLens folder. (Email us if you need them!)


Blast Off:
python app.py

Open http://localhost:5000 in your browser and have fun! 🎉


How to Use It

Sign Up: Make an account to start.
YouTube: Click “YouTube,” log in, and paste a video link to see comment magic.
Reddit: Go to “Reddit,” enter a post ID, and check out the insights.
Test It: Try the “debug” mode to play with fake comments.



🎥 See It Live
Check out our demo video to see CommentLens rock the comment world! (Add your video link here.) 🎬

🌟 What’s Coming Next?
We’re dreaming BIG for CommentLens! Here’s what’s on the way:

AI Tips: Groq AI will summarize comments and suggest video ideas.
Mood Vibes: Find out if fans are excited, mad, or curious.
Live Updates: Get comment alerts as they happen.
Fancy Charts: Add word clouds and interactive graphs.
More Languages: Catch rude comments in even more languages.
Cloud Fun: Run CommentLens online for everyone to use.


🤗 Help Us Grow
Love CommentLens? Join the fun and make it better! 🎈

Copy our code (fork the repo).
Add a cool feature: git checkout -b my-cool-idea.
Save it: git commit -m "Added cool idea".
Share it: git push origin my-cool-idea.
Tell us: Open a Pull Request.

See our Code of Conduct and report bugs at GitHub Issues.

📜 Free to Use
CommentLens is free for everyone under the MIT License. Play with it, share it, make it yours! 😄

👨‍🚀 Our Team

Tarun Goel - Code Wizard & Comment Tamer
Shubh Singhal


💬 Say Hi!
Got questions or ideas? Reach out:

GitHub: TarunGoel93
Email: goeltarun15@gmail.com
Issues: GitHub Issues



  Made with 💕 for YouTubers, Redditors, and dreamers everywhere! Let’s make comments FUN! 🌈
