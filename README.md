<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CommentLens README</title>
  <!-- Bootstrap 5 CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Font Awesome for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- AOS Animation Library -->
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <!-- Custom Styles -->
  <style>
    :root {
      --primary: #6366f1;
      --primary-light: #818cf8;
      --secondary: #10b981;
      --accent: #f59e0b;
      --dark: #1e293b;
      --light: #f8fafc;
      --gray: #64748b;
      --card-bg: #0f172a;
      --body-bg: #020617;
      --border-color: #334155;
    }
    
    body {
      background-color: var(--body-bg);
      font-family: 'Inter', sans-serif;
      color: var(--light);
      line-height: 1.7;
    }
    
    h1, h2, h3, h4, h5, h6 {
      font-family: 'Poppins', sans-serif;
      font-weight: 600;
    }
    
    .header {
      background: linear-gradient(120deg, rgba(99, 102, 241, 0.1), rgba(16, 185, 129, 0.1));
      border: 1px solid rgba(99, 102, 241, 0.2);
      border-radius: 16px;
      padding: 3rem 2rem;
      position: relative;
      overflow: hidden;
    }
    
    .header::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at top right, rgba(99, 102, 241, 0.15), transparent 70%);
      z-index: 0;
    }
    
    .header-content {
      position: relative;
      z-index: 1;
    }
    
    .badge-custom {
      background-color: rgba(99, 102, 241, 0.2);
      color: var(--primary-light);
      border: 1px solid rgba(99, 102, 241, 0.3);
      font-weight: 500;
      padding: 0.5rem 1rem;
      border-radius: 50px;
      margin-right: 0.5rem;
      transition: all 0.3s ease;
    }
    
    .badge-custom:hover {
      background-color: rgba(99, 102, 241, 0.3);
      transform: translateY(-2px);
    }
    
    .card {
      background-color: var(--card-bg);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      transition: all 0.4s ease;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .card:hover {
      transform: translateY(-5px);
      box-shadow: 0 10px 30px rgba(99, 102, 241, 0.15);
      border-color: rgba(99, 102, 241, 0.3);
    }
    
    .card-title {
      position: relative;
      display: inline-block;
      margin-bottom: 1.5rem;
      font-weight: 700;
    }
    
    .card-title::after {
      content: '';
      position: absolute;
      left: 0;
      bottom: -8px;
      height: 3px;
      width: 40px;
      background: var(--primary);
      border-radius: 3px;
    }
    
    .card-title.text-primary {
      color: var(--primary) !important;
    }
    
    .card-title.text-success {
      color: var(--secondary) !important;
    }
    
    .card-title.text-warning {
      color: var(--accent) !important;
    }
    
    .card-title.text-info {
      color: #0ea5e9 !important;
    }
    
    .card-title.text-danger {
      color: #ef4444 !important;
    }
    
    .btn-custom {
      background-color: var(--primary);
      color: white;
      border: none;
      border-radius: 8px;
      padding: 0.75rem 1.5rem;
      font-weight: 500;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
      z-index: 1;
    }
    
    .btn-custom::before {
      content: '';
      position: absolute;
      top: 0;
      left: -100%;
      width: 100%;
      height: 100%;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
      transition: all 0.5s ease;
      z-index: -1;
    }
    
    .btn-custom:hover {
      background-color: var(--primary-light);
      transform: translateY(-3px);
      box-shadow: 0 7px 14px rgba(99, 102, 241, 0.3);
      color: white;
    }
    
    .btn-custom:hover::before {
      left: 100%;
    }
    
    .section-divider {
      height: 1px;
      background: linear-gradient(90deg, transparent, var(--border-color), transparent);
      margin: 3rem 0;
      position: relative;
    }
    
    .section-divider::after {
      content: '';
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
      width: 10px;
      height: 10px;
      background-color: var(--primary);
      border-radius: 50%;
    }
    
    pre {
      background-color: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--border-color);
      border-radius: 8px;
      padding: 1rem;
      color: #e2e8f0;
      overflow-x: auto;
    }
    
    code {
      font-family: 'Courier New', monospace;
      color: #e2e8f0;
    }
    
    .feature-icon {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background-color: rgba(99, 102, 241, 0.1);
      color: var(--primary);
      margin-right: 1rem;
      transition: all 0.3s ease;
    }
    
    .feature-item {
      display: flex;
      align-items: flex-start;
      margin-bottom: 1.5rem;
      transition: all 0.3s ease;
    }
    
    .feature-item:hover .feature-icon {
      background-color: var(--primary);
      color: white;
      transform: scale(1.1);
    }
    
    .feature-content {
      flex: 1;
    }
    
    .img-container {
      border-radius: 12px;
      overflow: hidden;
      border: 1px solid var(--border-color);
      transition: all 0.3s ease;
    }
    
    .img-container:hover {
      transform: scale(1.02);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    a {
      color: var(--primary-light);
      text-decoration: none;
      transition: all 0.3s ease;
    }
    
    a:hover {
      color: var(--primary);
      text-decoration: underline;
    }
    
    .tech-badge {
      display: inline-flex;
      align-items: center;
      background-color: rgba(99, 102, 241, 0.1);
      color: var(--primary-light);
      border: 1px solid rgba(99, 102, 241, 0.2);
      border-radius: 50px;
      padding: 0.5rem 1rem;
      margin: 0.25rem;
      font-size: 0.85rem;
      transition: all 0.3s ease;
    }
    
    .tech-badge:hover {
      background-color: rgba(99, 102, 241, 0.2);
      transform: translateY(-2px);
    }
    
    .tech-badge i {
      margin-right: 0.5rem;
    }
    
    .team-member {
      display: flex;
      align-items: center;
      margin-bottom: 1rem;
    }
    
    .team-avatar {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background-color: var(--primary);
      color: white;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: bold;
      margin-right: 1rem;
    }
    
    .contact-item {
      display: flex;
      align-items: center;
      margin-bottom: 1rem;
    }
    
    .contact-icon {
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background-color: rgba(99, 102, 241, 0.1);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right: 1rem;
      transition: all 0.3s ease;
    }
    
    .contact-item:hover .contact-icon {
      background-color: var(--primary);
      color: white;
      transform: scale(1.1);
    }
    
    .footer {
      background: linear-gradient(120deg, rgba(99, 102, 241, 0.05), rgba(16, 185, 129, 0.05));
      border-top: 1px solid rgba(99, 102, 241, 0.1);
      border-radius: 12px;
      padding: 2rem;
      margin-top: 3rem;
    }
    
    /* Typing animation for header */
    .typing-text {
      border-right: 3px solid var(--primary);
      white-space: nowrap;
      overflow: hidden;
      animation: typing 4s steps(40) infinite, blink-caret 0.75s step-end infinite;
    }
    
    @keyframes typing {
      0%, 100% { width: 0 }
      50% { width: 100% }
    }
    
    @keyframes blink-caret {
      from, to { border-color: transparent }
      50% { border-color: var(--primary) }
    }
    
    /* Floating animation for cards */
    .floating {
      animation: floating 3s ease-in-out infinite;
    }
    
    @keyframes floating {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }
    
    /* Pulse animation for buttons */
    .pulse {
      animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
      0% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }
      70% { box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }
      100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
      .header {
        padding: 2rem 1rem;
      }
      
      .badge-custom {
        margin-bottom: 0.5rem;
      }
    }
  </style>
</head>
<body>
  <div class="container py-5">
    <!-- Header -->
    <div class="header mb-5" data-aos="fade-up">
      <div class="header-content text-center">
        <h1 class="display-4 mb-3">
          <i class="fas fa-comments text-primary me-2"></i>
          <span class="typing-text">CommentLens</span>
        </h1>
        <p class="lead mb-4">Intelligent Analysis for YouTube & Reddit Comments</p>
        <div class="d-flex flex-wrap justify-content-center mb-3">
          <span class="badge-custom" data-aos="fade-up" data-aos-delay="100">
            <i class="fas fa-certificate me-1"></i> MIT License
          </span>
          <span class="badge-custom" data-aos="fade-up" data-aos-delay="200">
            <i class="fab fa-python me-1"></i> Python 3.8+
          </span>
          <span class="badge-custom" data-aos="fade-up" data-aos-delay="300">
            <i class="fas fa-star me-1"></i> Star Us on GitHub
          </span>
        </div>
      </div>
    </div>

    <!-- What is CommentLens -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-primary">
          <i class="fas fa-lightbulb me-2"></i>What is CommentLens?
        </h2>
        <p class="card-text">
          CommentLens is an advanced analytics tool designed to help content creators understand and engage with their audience more effectively. By analyzing comments from YouTube videos and Reddit posts, CommentLens provides valuable insights into audience sentiment, questions, and trends.
        </p>
        <p class="card-text">
          Our platform uses natural language processing and machine learning to categorize comments, identify questions, detect inappropriate content, and extract key topics—transforming overwhelming comment sections into actionable intelligence for content strategy.
        </p>
        <div class="img-container mt-4" data-aos="zoom-in" data-aos-delay="200">
          <img src="https://via.placeholder.com/800x400.png?text=CommentLens+Dashboard" class="img-fluid" alt="CommentLens Dashboard">
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Problem -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-danger">
          <i class="fas fa-exclamation-triangle me-2"></i>The Challenge
        </h2>
        <p class="card-text">
          Content creators face significant challenges when managing audience engagement:
        </p>
        
        <div class="row mt-4">
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-right" data-aos-delay="100">
              <div class="feature-icon">
                <i class="fas fa-comments"></i>
              </div>
              <div class="feature-content">
                <h5>Volume Overload</h5>
                <p>Processing thousands of comments manually is time-consuming and inefficient.</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-left" data-aos-delay="200">
              <div class="feature-icon">
                <i class="fas fa-filter"></i>
              </div>
              <div class="feature-content">
                <h5>Content Moderation</h5>
                <p>Identifying and managing inappropriate comments to maintain a positive community.</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-right" data-aos-delay="300">
              <div class="feature-icon">
                <i class="fas fa-question-circle"></i>
              </div>
              <div class="feature-content">
                <h5>Missed Opportunities</h5>
                <p>Overlooking important questions and feedback that could inform future content.</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-left" data-aos-delay="400">
              <div class="feature-icon">
                <i class="fas fa-chart-line"></i>
              </div>
              <div class="feature-content">
                <h5>Trend Identification</h5>
                <p>Difficulty in spotting emerging topics and audience interests without proper tools.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Solution -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-success">
          <i class="fas fa-magic me-2"></i>Our Solution
        </h2>
        <p class="card-text">
          CommentLens transforms comment management with powerful analytics that provide actionable insights:
        </p>
        
        <div class="row mt-4">
          <div class="col-lg-6">
            <div class="feature-item" data-aos="fade-up" data-aos-delay="100">
              <div class="feature-icon">
                <i class="fas fa-heart"></i>
              </div>
              <div class="feature-content">
                <h5>Sentiment Analysis</h5>
                <p>Automatically categorize comments as positive, negative, or neutral to gauge audience reception.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-up" data-aos-delay="200">
              <div class="feature-icon">
                <i class="fas fa-question"></i>
              </div>
              <div class="feature-content">
                <h5>Question Detection</h5>
                <p>Identify questions from your audience to improve engagement and provide timely responses.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-up" data-aos-delay="300">
              <div class="feature-icon">
                <i class="fas fa-shield-alt"></i>
              </div>
              <div class="feature-content">
                <h5>Content Moderation</h5>
                <p>Detect potentially inappropriate comments across multiple languages to maintain community standards.</p>
              </div>
            </div>
          </div>
          
          <div class="col-lg-6">
            <div class="feature-item" data-aos="fade-up" data-aos-delay="400">
              <div class="feature-icon">
                <i class="fas fa-tags"></i>
              </div>
              <div class="feature-content">
                <h5>Topic Extraction</h5>
                <p>Discover frequently mentioned keywords and topics to inform your content strategy.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-up" data-aos-delay="500">
              <div class="feature-icon">
                <i class="fas fa-chart-pie"></i>
              </div>
              <div class="feature-content">
                <h5>Visual Analytics</h5>
                <p>Intuitive charts and visualizations that make complex data easy to understand at a glance.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-up" data-aos-delay="600">
              <div class="feature-icon">
                <i class="fas fa-robot"></i>
              </div>
              <div class="feature-content">
                <h5>AI-Powered Insights</h5>
                <p>Coming soon: Advanced AI summaries and content recommendations based on audience feedback.</p>
              </div>
            </div>
          </div>
        </div>
        
        <div class="text-center mt-4">
          <a href="#" class="btn btn-custom pulse" data-aos="zoom-in" data-aos-delay="700">
            <i class="fas fa-play me-2"></i>Watch Demo
          </a>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Tech Stack -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-info">
          <i class="fas fa-code me-2"></i>Technology Stack
        </h2>
        <p class="card-text">
          CommentLens is built with a modern, scalable technology stack:
        </p>
        
        <div class="d-flex flex-wrap justify-content-center mt-4">
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="100">
            <i class="fab fa-python"></i>Python
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="150">
            <i class="fab fa-flask"></i>Flask
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="200">
            <i class="fas fa-database"></i>SQLite
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="250">
            <i class="fab fa-youtube"></i>YouTube API
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="300">
            <i class="fab fa-reddit"></i>Reddit API
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="350">
            <i class="fas fa-brain"></i>Groq AI
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="400">
            <i class="fas fa-chart-bar"></i>Matplotlib
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="450">
            <i class="fas fa-language"></i>NLTK
          </span>
          <span class="tech-badge" data-aos="zoom-in" data-aos-delay="500">
            <i class="fas fa-robot"></i>Scikit-learn
          </span>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Benefits -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-primary">
          <i class="fas fa-award me-2"></i>Key Benefits
        </h2>
        
        <div class="row mt-4">
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-right" data-aos-delay="100">
              <div class="feature-icon">
                <i class="fas fa-clock"></i>
              </div>
              <div class="feature-content">
                <h5>Time Efficiency</h5>
                <p>Reduce hours spent manually reviewing comments to focus on content creation.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-right" data-aos-delay="200">
              <div class="feature-icon">
                <i class="fas fa-users"></i>
              </div>
              <div class="feature-content">
                <h5>Audience Engagement</h5>
                <p>Respond to questions and feedback promptly to build a loyal community.</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-left" data-aos-delay="300">
              <div class="feature-icon">
                <i class="fas fa-bullseye"></i>
              </div>
              <div class="feature-content">
                <h5>Content Strategy</h5>
                <p>Leverage audience insights to create more targeted and relevant content.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-left" data-aos-delay="400">
              <div class="feature-icon">
                <i class="fas fa-shield-alt"></i>
              </div>
              <div class="feature-content">
                <h5>Community Management</h5>
                <p>Maintain a positive environment by identifying problematic comments early.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Get Started -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-success">
          <i class="fas fa-rocket me-2"></i>Getting Started
        </h2>
        <p class="card-text">
          Follow these steps to set up CommentLens on your local machine:
        </p>
        
        <h5 class="mt-4 mb-3"><i class="fas fa-list-ul me-2"></i>Prerequisites</h5>
        <ul>
          <li>Python 3.8 or higher</li>
          <li>Git</li>
          <li>YouTube API credentials</li>
          <li>Reddit API credentials</li>
        </ul>
        
        <h5 class="mt-4 mb-3"><i class="fas fa-terminal me-2"></i>Installation</h5>
        
        <div class="mb-3" data-aos="fade-up" data-aos-delay="100">
          <p><strong>1. Clone the repository</strong></p>
          <pre><code>git clone https://github.com/TarunGoel93/CommentLens.git
cd CommentLens</code></pre>
        </div>
        
        <div class="mb-3" data-aos="fade-up" data-aos-delay="200">
          <p><strong>2. Create a virtual environment</strong></p>
          <pre><code>python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate</code></pre>
        </div>
        
        <div class="mb-3" data-aos="fade-up" data-aos-delay="300">
          <p><strong>3. Install dependencies</strong></p>
          <pre><code>pip install flask flask-sqlalchemy bcrypt google-auth-oauthlib google-api-python-client sumy asyncpraw nltk matplotlib scikit-learn requests python-dotenv</code></pre>
        </div>
        
        <div class="mb-3" data-aos="fade-up" data-aos-delay="400">
          <p><strong>4. Download NLTK resources</strong></p>
          <pre><code>python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"</code></pre>
        </div>
        
        <div class="mb-3" data-aos="fade-up" data-aos-delay="500">
          <p><strong>5. Configure API credentials</strong></p>
          <p>Create a <code>.env</code> file in the project root:</p>
          <pre><code>REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
GROQ_API_KEY=your_key</code></pre>
          <p>Add your <code>client_secret.json</code> file for YouTube API in the project root.</p>
        </div>
        
        <div class="mb-3" data-aos="fade-up" data-aos-delay="600">
          <p><strong>6. Add model files</strong></p>
          <p>Place <code>classifier.pkl</code> and <code>tfidf_vectorizer.pkl</code> in the project root directory.</p>
        </div>
        
        <div class="mb-3" data-aos="fade-up" data-aos-delay="700">
          <p><strong>7. Launch the application</strong></p>
          <pre><code>python app.py</code></pre>
          <p>Access the application at <code>http://localhost:5000</code></p>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Screenshots -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-warning">
          <i class="fas fa-images me-2"></i>Screenshots
        </h2>
        
        <div class="row mt-4">
          <div class="col-md-6 mb-4" data-aos="zoom-in" data-aos-delay="100">
            <div class="img-container">
              <img src="https://via.placeholder.com/600x400.png?text=Dashboard+View" class="img-fluid" alt="Dashboard View">
            </div>
            <p class="text-center mt-2">Dashboard Overview</p>
          </div>
          
          <div class="col-md-6 mb-4" data-aos="zoom-in" data-aos-delay="200">
            <div class="img-container">
              <img src="https://via.placeholder.com/600x400.png?text=Sentiment+Analysis" class="img-fluid" alt="Sentiment Analysis">
            </div>
            <p class="text-center mt-2">Sentiment Analysis</p>
          </div>
          
          <div class="col-md-6 mb-4" data-aos="zoom-in" data-aos-delay="300">
            <div class="img-container">
              <img src="https://via.placeholder.com/600x400.png?text=Topic+Extraction" class="img-fluid" alt="Topic Extraction">
            </div>
            <p class="text-center mt-2">Topic Extraction</p>
          </div>
          
          <div class="col-md-6 mb-4" data-aos="zoom-in" data-aos-delay="400">
            <div class="img-container">
              <img src="https://via.placeholder.com/600x400.png?text=Comment+Moderation" class="img-fluid" alt="Comment Moderation">
            </div>
            <p class="text-center mt-2">Comment Moderation</p>
          </div>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Roadmap -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-info">
          <i class="fas fa-map me-2"></i>Roadmap
        </h2>
        <p class="card-text">
          We're continuously improving CommentLens with new features and capabilities:
        </p>
        
        <div class="row mt-4">
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-right" data-aos-delay="100">
              <div class="feature-icon">
                <i class="fas fa-robot"></i>
              </div>
              <div class="feature-content">
                <h5>AI-Powered Summaries</h5>
                <p>Automated comment summaries and content recommendations.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-right" data-aos-delay="200">
              <div class="feature-icon">
                <i class="fas fa-globe"></i>
              </div>
              <div class="feature-content">
                <h5>Multilingual Support</h5>
                <p>Expanded language detection and analysis capabilities.</p>
              </div>
            </div>
          </div>
          
          <div class="col-md-6">
            <div class="feature-item" data-aos="fade-left" data-aos-delay="300">
              <div class="feature-icon">
                <i class="fas fa-bell"></i>
              </div>
              <div class="feature-content">
                <h5>Real-time Notifications</h5>
                <p>Alerts for important comments and engagement opportunities.</p>
              </div>
            </div>
            
            <div class="feature-item" data-aos="fade-left" data-aos-delay="400">
              <div class="feature-icon">
                <i class="fas fa-cloud"></i>
              </div>
              <div class="feature-content">
                <h5>Advanced Visualizations</h5>
                <p>Word clouds, trend analysis, and interactive dashboards.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Contribute -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-primary">
          <i class="fas fa-hands-helping me-2"></i>Contributing
        </h2>
        <p class="card-text">
          We welcome contributions from the community! Here's how you can help:
        </p>
        
        <ol class="mt-4">
          <li data-aos="fade-up" data-aos-delay="100">Fork the repository on GitHub</li>
          <li data-aos="fade-up" data-aos-delay="150">Create a new feature branch: <code>git checkout -b feature/amazing-feature</code></li>
          <li data-aos="fade-up" data-aos-delay="200">Commit your changes: <code>git commit -m 'Add some amazing feature'</code></li>
          <li data-aos="fade-up" data-aos-delay="250">Push to the branch: <code>git push origin feature/amazing-feature</code></li>
          <li data-aos="fade-up" data-aos-delay="300">Open a Pull Request</li>
        </ol>
        
        <p class="mt-3" data-aos="fade-up" data-aos-delay="350">
          Please read our <a href="CODE_OF_CONDUCT.md">Code of Conduct</a> before contributing. For major changes, please open an issue first to discuss what you would like to change.
        </p>
        
        <p data-aos="fade-up" data-aos-delay="400">
          Report bugs or request features through our <a href="https://github.com/TarunGoel93/CommentLens/issues">GitHub Issues</a> page.
        </p>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- License -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-success">
          <i class="fas fa-file-contract me-2"></i>License
        </h2>
        <p class="card-text">
          CommentLens is open-source software licensed under the <a href="LICENSE">MIT License</a>. This means you are free to use, modify, and distribute the software, even for commercial purposes, as long as you include the original copyright notice and license terms.
        </p>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Team -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-warning">
          <i class="fas fa-users me-2"></i>Team
        </h2>
        
        <div class="mt-4">
          <div class="team-member" data-aos="fade-up" data-aos-delay="100">
            <div class="team-avatar">TG</div>
            <div>
              <h5 class="mb-1">Tarun Goel</h5>
              <p class="text-muted mb-0">Lead Developer & Project Architect</p>
            </div>
          </div>
          
          <p class="mt-3" data-aos="fade-up" data-aos-delay="200">
            Want to join our team? <a href="https://github.com/TarunGoel93/CommentLens">Contribute to the project</a> and become a part of CommentLens!
          </p>
        </div>
      </div>
    </div>

    <div class="section-divider"></div>

    <!-- Contact -->
    <div class="card mb-4" data-aos="fade-up">
      <div class="card-body">
        <h2 class="card-title text-danger">
          <i class="fas fa-envelope me-2"></i>Contact
        </h2>
        
        <div class="mt-4">
          <div class="contact-item" data-aos="fade-up" data-aos-delay="100">
            <div class="contact-icon">
              <i class="fab fa-github"></i>
            </div>
            <div>
              <h5 class="mb-1">GitHub</h5>
              <p class="mb-0"><a href="https://github.com/TarunGoel93">TarunGoel93</a></p>
            </div>
          </div>
          
          <div class="contact-item" data-aos="fade-up" data-aos-delay="200">
            <div class="contact-icon">
              <i class="fas fa-envelope"></i>
            </div>
            <div>
              <h5 class="mb-1">Email</h5>
              <p class="mb-0"><a href="mailto:your.email@example.com">your.email@example.com</a></p>
            </div>
          </div>
          
          <div class="contact-item" data-aos="fade-up" data-aos-delay="300">
            <div class="contact-icon">
              <i class="fas fa-bug"></i>
            </div>
            <div>
              <h5 class="mb-1">Issues & Feature Requests</h5>
              <p class="mb-0"><a href="https://github.com/TarunGoel93/CommentLens/issues">GitHub Issues</a></p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <div class="footer text-center" data-aos="fade-up">
      <p class="mb-0">
        <i class="fas fa-code me-2"></i>Crafted with passion for content creators worldwide
      </p>
      <p class="mb-0 mt-2">
        <span class="badge-custom">
          <i class="fas fa-star me-1"></i> Star us on GitHub
        </span>
      </p>
    </div>
  </div>

  <!-- Bootstrap JS -->
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <!-- AOS Animation Library -->
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <!-- Custom JS -->
  <script>
    // Initialize AOS animation library
    document.addEventListener('DOMContentLoaded', function() {
      AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true
      });
      
      // Add floating animation to cards
      const cards = document.querySelectorAll('.card');
      cards.forEach((card, index) => {
        if (index % 2 === 0) {
          card.classList.add('floating');
        }
      });
      
      // Add hover effects for feature items
      const featureItems = document.querySelectorAll('.feature-item');
      featureItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
          this.style.transform = 'translateX(5px)';
        });
        item.addEventListener('mouseleave', function() {
          this.style.transform = 'translateX(0)';
        });
      });
    });
  </script>
</body>
</html>
