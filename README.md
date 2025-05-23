<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CommentLens README</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body {
      background: linear-gradient(135deg, #ff6b6b, #4ecdc4);
      font-family: 'Arial', sans-serif;
    }
    .jumbotron {
      background: linear-gradient(45deg, #ff1493, #00f7ff);
      color: white;
      text-shadow: 2px 2px #333;
      border-radius: 15px;
    }
    .card {
      transition: transform 0.3s, box-shadow 0.3s;
    }
    .card:hover {
      transform: scale(1.05);
      box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    .badge-custom {
      background-color: #ffd700;
      color: #333;
    }
    .btn-custom {
      background-color: #ff4500;
      border: none;
    }
    .btn-custom:hover {
      background-color: #ff6347;
    }
    .section-divider {
      border-top: 3px dashed #ff69b4;
      margin: 2rem 0;
    }
  </style>
</head>
<body>
  <div class="container py-5">
    <div class="jumbotron text-center mb-5">
      <h1 class="display-4">🎉 CommentLens 🌟</h1>
      <p class="lead">Your Super Fun Tool to Make YouTube & Reddit Comments Awesome! 🚀</p>
      <div>
        <span class="badge badge-custom me-2">MIT License</span>
        <span class="badge badge-custom me-2">Python 3.8+</span>
        <span class="badge badge-custom">Star Us! ⭐</span>
      </div>
    </div>

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-primary">🌈 What’s CommentLens?</h2>
        <p class="card-text">
          Got a YouTube video or Reddit post with TONS of comments? 😲 Some are sweet 😍, some are rude 😣, and others are questions like “What’s next?” Reading them all is super hard! 😩
        </p>
        <p class="card-text">
          <strong>CommentLens</strong> is like a magic wand! 🪄 It’s a web app that checks your comments and tells you what’s going on. It finds happy fans, spots questions, and catches mean comments, then shows you cool charts and ideas to make your content AMAZING. It’s your new best friend for being a creator! 🦸‍♀️
        </p>
        <img src="../assets/demo.gif" class="img-fluid rounded mt-3" alt="CommentLens Demo">
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-danger">😩 Why You Need Help</h2>
        <p class="card-text">
          If you make videos or posts, comments are a big deal! But there’s a problem:
        </p>
        <ul>
          <li><strong>Too Many!</strong> Reading thousands takes forever. ⏳</li>
          <li><strong>Mean Ones!</strong> Rude comments can make fans sad. 😞</li>
          <li><strong>Missed Ideas!</strong> You might skip questions or cool tips. 💡</li>
        </ul>
        <p class="card-text">
          Sorting comments by hand is no fun. You need a quick way to understand your fans! 😊
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-success">🎨 How CommentLens Saves the Day</h2>
        <p class="card-text">
          CommentLens is like a superhero for your comments! 🦸‍♂️ It looks at up to 500 comments (100 for free) and shows you:
        </p>
        <ul>
          <li><strong>Mood Check</strong>: Are fans happy 😄, upset 😞, or chill 😐?</li>
          <li><strong>Questions</strong>: Finds “What’s this?” so you can reply.</li>
          <li><strong>Rude Alerts</strong>: Spots mean comments (even in Hindi!) to keep things nice.</li>
          <li><strong>Hot Words</strong>: Shows words like “funny” to plan your next post.</li>
          <li><strong>Smart Tips</strong> (Soon): Groq AI will give you summaries and ideas!</li>
        </ul>
        <div class="text-center">
          <a href="#" class="btn btn-custom mt-3">🎥 Watch Our Demo!</a>
        </div>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-warning">🌟 Cool Stuff It Does</h2>
        <div class="row">
          <div class="col-md-6">
            <p>🌍 Grabs comments super fast!</p>
            <p>😎 Sorts into happy or sad vibes.</p>
            <p>🛑 Catches rude comments.</p>
          </div>
          <div class="col-md-6">
            <p>🔍 Finds popular words.</p>
            <p>📊 Shows colorful charts.</p>
            <p>🧠 Adds smart AI tips (soon)!</p>
          </div>
        </div>
        <img src="../assets/dashboard.png" class="img-fluid rounded mt-3" alt="Dashboard">
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-info">🧰 What’s It Made Of?</h2>
        <p class="card-text">
          CommentLens uses fun tools to work its magic! 🌟
        </p>
        <ul>
          <li><strong>Python</strong>: Coding superhero! 🐍</li>
          <li><strong>Flask</strong>: Makes the app fast.</li>
          <li><strong>SQLite</strong>: Saves account info.</li>
          <li><strong>YouTube & Reddit Tools</strong>: Grab comments.</li>
          <li><strong>Groq AI</strong> (Soon): Smart tips.</li>
          <li><strong>Smart Readers</strong>: Guess moods.</li>
          <li><strong>Charts</strong>: Pretty pictures.</li>
          <li><strong>Web Design</strong>: Looks awesome!</li>
        </ul>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-primary">💫 Why You’ll Love It</h2>
        <p class="card-text">
          CommentLens makes being a creator EASY:
        </p>
        <ul>
          <li><strong>Saves Time</strong>: No reading all day!</li>
          <li><strong>Happy Fans</strong>: Answer questions.</li>
          <li><strong>Bigger Channel</strong>: Make hits.</li>
          <li><strong>Fun Vibes</strong>: Friendly comments.</li>
        </ul>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-success">🚀 Try It Out!</h2>
        <p class="card-text">
          Want to play with CommentLens? Here’s how! 🖥️
        </p>
        <h4>You Need:</h4>
        <ul>
          <li>Python 3.8 or newer.</li>
          <li>Git to grab code.</li>
          <li>YouTube/Reddit keys.</li>
          <li>Two files (we’ll share).</li>
        </ul>
        <h4>Steps:</h4>
        <ol>
          <li><strong>Get Code</strong>:<pre><code>git clone https://github.com/TarunGoel93/CommentLens.git
cd CommentLens</code></pre></li>
          <li><strong>Safe Space</strong>:<pre><code>python -m venv venv
source venv/bin/activate</code></pre></li>
          <li><strong>Add Tools</strong>:<pre><code>pip install flask flask-sqlalchemy bcrypt google-auth-oauthlib google-api-python-client sumy asyncpraw nltk matplotlib scikit-learn requests python-dotenv</code></pre></li>
          <li><strong>Grab Extras</strong>:<pre><code>python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"</code></pre></li>
          <li><strong>Add Secrets</strong>:<p>Put <code>client_secret.json</code> in folder. Make <code>.env</code>:<pre><code>REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
GROQ_API_KEY=your_key</code></pre></p></li>
          <li><strong>Add Files</strong>: Drop <code>classifier.pkl</code>, <code>tfidf_vectorizer.pkl</code>.</li>
          <li><strong>Start</strong>:<pre><code>python app.py</code></pre><p>Visit <code>http://localhost:5000</code>! 🎉</p></li>
        </ol>
        <h4>Use It:</h4>
        <p>Sign up, paste a video/post link, see insights!</p>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body text-center">
        <h2 class="card-title text-warning">📷 Sneak Peek</h2>
        <div class="row">
          <div class="col-md-6 mb-3">
            <img src="../assets/dashboard.png" class="img-fluid rounded" alt="Dashboard">
            <p>Dashboard</p>
          </div>
          <div class="col-md-6 mb-3">
            <img src="../assets/results.png" class="img-fluid rounded" alt="Results">
            <p>Results</p>
          </div>
        </div>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-info">🌟 What’s Next?</h2>
        <p class="card-text">
          Coming soon:
        </p>
        <ul>
          <li>AI tips for summaries, video ideas.</li>
          <li>Find excited or curious fans.</li>
          <li>Live comment alerts.</li>
          <li>Fancy charts like word clouds.</li>
          <li>More languages.</li>
        </ul>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-primary">🤗 Help Us Grow</h2>
        <p class="card-text">
          Love CommentLens? Add your magic! 🎈
        </p>
        <ol>
          <li>Fork on GitHub.</li>
          <li>Add feature: <code>git checkout -b my-idea</code>.</li>
          <li>Save: <code>git commit -m "Added idea"</code>.</li>
          <li>Share: <code>git push origin my-idea</code>.</li>
          <li>Open Pull Request.</li>
        </ol>
        <p class="card-text">
          See <a href="../CODE_OF_CONDUCT.md">Code of Conduct</a>, report bugs <a href="https://github.com/TarunGoel93/CommentLens/issues">here</a>.
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-success">📜 Free to Use</h2>
        <p class="card-text">
          Free under <a href="../LICENSE">MIT License</a>. Use, change, share! 😄
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-warning">👨‍🚀 Our Team</h2>
        <p class="card-text">
          - <strong>Tarun Goel</strong>: Code Wizard<br>
          - Add team here!
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-danger">💬 Say Hi!</h2>
        <p class="card-text">
          Ideas? Reach out:
        </p>
        <ul>
          <li><strong>GitHub</strong>: <a href="https://github.com/TarunGoel93">TarunGoel93</a></li>
          <li><strong>Email</strong>: your.email@example.com</li>
          <li><strong>Issues</strong>: <a href="https://github.com/TarunGoel93/CommentLens/issues">GitHub Issues</a></li>
        </ul>
      </div>
    </div>

    <div class="text-center mt-5">
      <p style="color: white; text-shadow: 1px 1px #333;">
        Made with 💕 for creators! Let’s make comments FUN! 🌈
      </p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
