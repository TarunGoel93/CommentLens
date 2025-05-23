<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CommentLens README</title>
  <!-- Bootstrap 5 CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom Styles -->
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
    <!-- Header -->
    <div class="jumbotron text-center mb-5">
      <h1 class="display-4">🎉 CommentLens 🌟</h1>
      <p class="lead">Your Super Fun Tool to Make YouTube & Reddit Comments Awesome! 🚀</p>
      <div>
        <span class="badge badge-custom me-2">MIT License</span>
        <span class="badge badge-custom me-2">Python 3.8+</span>
        <span class="badge badge-custom">Star Us! ⭐</span>
      </div>
    </div>

    <!-- What is CommentLens -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-primary">🌈 What’s CommentLens?</h2>
        <p class="card-text">
          Got a YouTube video or Reddit post with TONS of comments? 😲 Some are sweet 😍, some are rude 😣, and others are questions like “What’s next?” Reading them all is super hard! 😩
        </p>
        <p class="card-text">
          <strong>CommentLens</strong> is like a magic wand! 🪄 It’s a web app that checks your comments and tells you what’s going on. It finds happy fans, spots questions, and catches mean comments, then shows you cool charts and ideas to make your content AMAZING. It’s your new best friend for being a creator! 🦸‍♀️
        </p>
        <img src="https://via.placeholder.com/800x400.png?text=CommentLens+Magic+GIF" class="img-fluid rounded mt-3" alt="CommentLens Demo">
      </div>
    </div>

    <hr class="section-divider">

    <!-- Problem -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-danger">😩 Why You Need Help</h2>
        <p class="card-text">
          If you make videos or posts, comments are a big deal! But there’s a problem:
        </p>
        <ul>
          <li><strong>Too Many!</strong> Reading thousands of comments takes forever. ⏳</li>
          <li><strong>Mean Ones!</strong> Rude comments can make your fans sad. 😞</li>
          <li><strong>Missed Ideas!</strong> You might skip questions or cool tips for your next hit. 💡</li>
        </ul>
        <p class="card-text">
          Sorting comments by hand is no fun. You need a quick way to understand your fans and keep things happy! 😊
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Solution -->
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
          <li><strong>Hot Words</strong>: Shows words like “funny” or “tutorial” to plan your next post.</li>
          <li><strong>Smart Tips</strong> (Soon): Groq AI will give you short summaries and ideas!</li>
        </ul>
        <p class="card-text">
          It’s easy, saves time, and makes your fans LOVE you! 💖
        </p>
        <div class="text-center">
          <a href="#" class="btn btn-custom mt-3">🎥 Watch Our Demo!</a>
        </div>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Features -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-warning">🌟 Cool Stuff CommentLens Does</h2>
        <div class="row">
          <div class="col-md-6">
            <p>🌍 Grabs comments from YouTube or Reddit in a flash!</p>
            <p>😎 Sorts comments into happy, sad, or neutral vibes.</p>
            <p>🛑 Catches rude comments to keep your page friendly.</p>
          </div>
          <div class="col-md-6">
            <p>🔍 Finds popular words to spark new ideas.</p>
            <p>📊 Shows colorful charts of what fans feel.</p>
            <p>🧠 Adds smart AI tips (coming soon)!</p>
          </div>
        </div>
        <img src="https://via.placeholder.com/400x300.png?text=CommentLens+Dashboard" class="img-fluid rounded mt-3" alt="Dashboard">
      </div>
    </div>

    <hr class="section-divider">

    <!-- Tech Stack -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-info">🧰 What’s It Made Of?</h2>
        <p class="card-text">
          CommentLens is built with fun tools that make it shine! 🌟
        </p>
        <ul>
          <li><strong>Python</strong>: Our coding superhero! 🐍</li>
          <li><strong>Flask</strong>: Makes our app fast and cool.</li>
          <li><strong>SQLite</strong>: Saves your account info safely.</li>
          <li><strong>YouTube & Reddit Tools</strong>: Grabs comments like magic.</li>
          <li><strong>Groq AI</strong> (Soon): Gives smart tips for your content.</li>
          <li><strong>Smart Readers</strong>: Guess comment moods with brainy tricks.</li>
          <li><strong>Charts</strong>: Draws pretty pictures of fan feelings.</li>
          <li><strong>Web Design</strong>: Makes everything look awesome!</li>
        </ul>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Why Love It -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-primary">💫 Why You’ll Love It</h2>
        <p class="card-text">
          CommentLens makes being a creator SO much easier:
        </p>
        <ul>
          <li><strong>Saves Time</strong>: No more reading comments all day!</li>
          <li><strong>Happy Fans</strong>: Answer questions and keep things nice.</li>
          <li><strong>Bigger Channel</strong>: Use fan ideas to make hits.</li>
          <li><strong>Fun Vibes</strong>: Creates a friendly comment zone.</li>
        </ul>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Get Started -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-success">🚀 Try It Out!</h2>
        <p class="card-text">
          Want to play with CommentLens? Here’s how to set it up! 🖥️
        </p>
        <h4>You Need:</h4>
        <ul>
          <li>Python 3.8 or newer.</li>
          <li>Git to grab our code.</li>
          <li>YouTube and Reddit keys (ask Google/Reddit for them).</li>
          <li>Two special files (we’ll share them).</li>
        </ul>
        <h4>Steps:</h4>
        <ol>
          <li>
            <strong>Get the Code</strong>:
            <pre><code>git clone https://github.com/TarunGoel93/CommentLens.git
cd CommentLens</code></pre>
          </li>
          <li>
            <strong>Make a Safe Space</strong>:
            <pre><code>python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate</code></pre>
          </li>
          <li>
            <strong>Add Tools</strong>:
            <pre><code>pip install flask flask-sqlalchemy bcrypt google-auth-oauthlib google-api-python-client sumy asyncpraw nltk matplotlib scikit-learn requests python-dotenv</code></pre>
          </li>
          <li>
            <strong>Grab Extras</strong>:
            <pre><code>python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"</code></pre>
          </li>
          <li>
            <strong>Add Secrets</strong>:
            <p>Put <code>client_secret.json</code> in the folder. Make a <code>.env</code> file:</p>
            <pre><code>REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
GROQ_API_KEY=your_key</code></pre>
          </li>
          <li>
            <strong>Add Files</strong>: Drop <code>classifier.pkl</code> and <code>tfidf_vectorizer.pkl</code> in the folder. (Ask us for them!)
          </li>
          <li>
            <strong>Start It</strong>:
            <pre><code>python app.py</code></pre>
            <p>Visit <code>http://localhost:5000</code> and have fun! 🎉</p>
          </li>
        </ol>
        <h4>How to Use:</h4>
        <p>Sign up, paste a YouTube video link or Reddit post ID, and see cool comment insights!</p>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Screenshots -->
    <div class="card mb-4">
      <div class="card-body text-center">
        <h2 class="card-title text-warning">📷 Sneak Peek</h2>
        <div class="row">
          <div class="col-md-6 mb-3">
            <img src="https://via.placeholder.com/400x300.png?text=CommentLens+Dashboard" class="img-fluid rounded" alt="Dashboard">
            <p>Dashboard</p>
          </div>
          <div class="col-md-6 mb-3">
            <img src="https://via.placeholder.com/400x300.png?text=Cool+Results" class="img-fluid rounded" alt="Results">
            <p>Results</p>
          </div>
        </div>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Future Plans -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-info">🌟 What’s Next?</h2>
        <p class="card-text">
          We’re making CommentLens even cooler! Coming soon:
        </p>
        <ul>
          <li>AI tips to summarize comments and suggest videos.</li>
          <li>Find out if fans are excited or curious.</li>
          <li>Live comment alerts.</li>
          <li>Fancy charts like word clouds.</li>
          <li>Support for more languages.</li>
        </ul>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Contribute -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-primary">🤗 Help Us Grow</h2>
        <p class="card-text">
          Love CommentLens? Add your magic! 🎈
        </p>
        <ol>
          <li>Copy our code (fork on GitHub).</li>
          <li>Add a feature: <code>git checkout -b my-idea</code>.</li>
          <li>Save it: <code>git commit -m "Added idea"</code>.</li>
          <li>Share: <code>git push origin my-idea</code>.</li>
          <li>Tell us: Open a Pull Request.</li>
        </ol>
        <p class="card-text">
          Check our <a href="CODE_OF_CONDUCT.md">Code of Conduct</a> and report bugs <a href="https://github.com/TarunGoel93/CommentLens/issues">here</a>.
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <!-- License -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-success">📜 Free to Use</h2>
        <p class="card-text">
          CommentLens is free for all under the <a href="LICENSE">MIT License</a>. Use it, change it, share it! 😄
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Team -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-warning">👨‍🚀 Our Team</h2>
        <p class="card-text">
          - <strong>Tarun Goel</strong>: Code Wizard & Comment Tamer<br>
          - Add your team here!
        </p>
      </div>
    </div>

    <hr class="section-divider">

    <!-- Contact -->
    <div class="card mb-4">
      <div class="card-body">
        <h2 class="card-title text-danger">💬 Say Hi!</h2>
        <p class="card-text">
          Got ideas? Reach out:
        </p>
        <ul>
          <li><strong>GitHub</strong>: <a href="https://github.com/TarunGoel93">TarunGoel93</a></li>
          <li><strong>Email</strong>: your.email@example.com</li>
          <li><strong>Issues</strong>: <a href="https://github.com/TarunGoel93/CommentLens/issues">GitHub Issues</a></li>
        </ul>
      </div>
    </div>

    <!-- Footer -->
    <div class="text-center mt-5">
      <p style="color: white; text-shadow: 1px 1px #333;">
        Made with 💕 for creators everywhere! Let’s make comments FUN! 🌈
      </p>
    </div>
  </div>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
