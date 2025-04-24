document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.querySelector(".menu-toggle");
  const navLinks = document.querySelector(".nav-links");

  menuToggle.addEventListener("click", function () {
    navLinks.classList.toggle("active");
  });

  // Smooth scrolling for navigation links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      document.querySelector(this.getAttribute("href")).scrollIntoView({
        behavior: "smooth",
      });
    });
  });

  // Animate elements on scroll
  const animateOnScroll = (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("active");
        observer.unobserve(entry.target);
      }
    });
  };

  const animationObserver = new IntersectionObserver(animateOnScroll, {
    root: null,
    threshold: 0.1,
  });

  document.querySelectorAll(".animate-on-scroll").forEach((el) => {
    animationObserver.observe(el);
  });

  // Highlight active navigation link based on scroll position
  const sections = document.querySelectorAll("section");
  const navItems = document.querySelectorAll(".nav-links a");

  const highlightNavOnScroll = () => {
    let current = "";
    sections.forEach((section) => {
      const sectionTop = section.offsetTop;
      if (pageYOffset >= sectionTop - 60) {
        current = section.getAttribute("id");
      }
    });

    navItems.forEach((item) => {
      item.classList.remove("active");
      if (item.getAttribute("href") === `#${current}`) {
        item.classList.add("active");
      }
    });
  };

  window.addEventListener("scroll", highlightNavOnScroll);

  // Sample comment analysis (unchanged)
  const sampleComment = document.getElementById("sample-comment");
  const analyzeButton = document.getElementById("analyze-button");
  const sentimentResult = document.getElementById("sentiment-result");

  analyzeButton.addEventListener("click", () => {
    const comment = sampleComment.value.trim();
    if (comment) {
      // Simulate AI analysis (replace with actual API call in production)
      const sentiments = ["Positive", "Neutral", "Negative"];
      const randomSentiment =
        sentiments[Math.floor(Math.random() * sentiments.length)];
      sentimentResult.textContent = `Sentiment: ${randomSentiment}`;
      sentimentResult.style.color =
        randomSentiment === "Positive"
          ? "#4CAF50"
          : randomSentiment === "Negative"
          ? "#F44336"
          : "#FFC107";
    } else {
      sentimentResult.textContent = "Please enter a comment to analyze.";
      sentimentResult.style.color = "#333333";
    }
  });
});

// document.addEventListener("DOMContentLoaded", function () {
//   const menuToggle = document.querySelector(".menu-toggle");
//   const navLinks = document.querySelector(".nav-links");

//   menuToggle.addEventListener("click", function () {
//     navLinks.classList.toggle("active");
//   });
// });


// document.addEventListener("DOMContentLoaded", () => {
//   // Smooth scrolling for navigation links
//   document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
//     anchor.addEventListener("click", function (e) {
//       e.preventDefault();
//       document.querySelector(this.getAttribute("href")).scrollIntoView({
//         behavior: "smooth",
//       });
//     });
//   });

//   // Animate feature cards on scroll
//   const featureCards = document.querySelectorAll(".feature-card");
//   const animateOnScroll = (entries, observer) => {
//     entries.forEach((entry) => {
//       if (entry.isIntersecting) {
//         entry.target.classList.add("animate");
//         observer.unobserve(entry.target);
//       }
//     });
//   };

//   const featureObserver = new IntersectionObserver(animateOnScroll, {
//     root: null,
//     threshold: 0.1,
//   });

//   featureCards.forEach((card) => {
//     featureObserver.observe(card);
//   });

//   // Highlight active navigation link based on scroll position
//   const sections = document.querySelectorAll("section");
//   const navLinks = document.querySelectorAll(".nav-links a");

//   const highlightNavOnScroll = () => {
//     const scrollPosition = window.scrollY;

//     sections.forEach((section) => {
//       const sectionTop = section.offsetTop - 100;
//       const sectionHeight = section.clientHeight;
//       const sectionId = section.getAttribute("id");

//       if (
//         scrollPosition >= sectionTop &&
//         scrollPosition < sectionTop + sectionHeight
//       ) {
//         navLinks.forEach((link) => {
//           link.classList.remove("active");
//           if (link.getAttribute("href") === `#${sectionId}`) {
//             link.classList.add("active");
//           }
//         });
//       }
//     });
//   };

//   window.addEventListener("scroll", highlightNavOnScroll);

//   // Sample comment analysis
//   const sampleComment = document.getElementById("sample-comment");
//   const analyzeButton = document.getElementById("analyze-button");
//   const sentimentResult = document.getElementById("sentiment-result");

//   analyzeButton.addEventListener("click", () => {
//     const comment = sampleComment.value.trim();
//     if (comment) {
//       // Simulate AI analysis (replace with actual API call in production)
//       const sentiments = ["Positive", "Neutral", "Negative"];
//       const randomSentiment =
//         sentiments[Math.floor(Math.random() * sentiments.length)];
//       sentimentResult.textContent = `Sentiment: ${randomSentiment}`;
//       sentimentResult.style.color =
//         randomSentiment === "Positive"
//           ? "#4CAF50"
//           : randomSentiment === "Negative"
//           ? "#F44336"
//           : "#FFC107";
//     } else {
//       sentimentResult.textContent = "Please enter a comment to analyze.";
//       sentimentResult.style.color = "#333333";
//     }
//   });
// });
