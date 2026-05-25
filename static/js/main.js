// Grissom Corporate Services - Main JavaScript

// Progress Bar
const progressBar = document.getElementById('progress-bar');
window.addEventListener('scroll', () => {
  const scrollPercentage = (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100;
  progressBar.style.width = scrollPercentage + '%';
});

// Navigation
const mainNav = document.getElementById('main-nav');
const navLogo = document.getElementById('nav-logo');
const navContact = document.getElementById('nav-contact');

window.addEventListener('scroll', () => {
  if (window.scrollY > 100) {
    mainNav.classList.add('scrolled');
  } else {
    mainNav.classList.remove('scrolled');
  }
});

// Show nav elements on page load
setTimeout(() => {
  navLogo.classList.add('visible');
  navContact.classList.add('visible');
}, 100);

// Intersection Observer for animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -100px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe elements for animations
document.querySelectorAll('.wwd-photo, .wwd-right, .approach-section, .approach-card, .enquiries-section, footer').forEach(el => {
  observer.observe(el);
});

// Hero section animations
const heroEyebrow = document.querySelector('.hero-eyebrow');
const titleWords = document.querySelectorAll('.title-word');
const heroSubtitle = document.querySelector('.hero-subtitle');
const heroRight = document.querySelector('.hero-right');
const heroIntro = document.querySelector('.hero-intro');
const dividerLine = document.querySelector('.divider-line');
const heroBody = document.querySelector('.hero-body');
const approachLabel = document.querySelector('.approach-over-label');
const approachQuote = document.querySelector('.approach-big-quote');

setTimeout(() => {
  if (heroEyebrow) heroEyebrow.classList.add('revealed');
}, 200);

setTimeout(() => {
  titleWords.forEach(word => word.classList.add('revealed'));
}, 300);

setTimeout(() => {
  if (heroSubtitle) heroSubtitle.classList.add('revealed');
}, 850);

setTimeout(() => {
  if (heroRight) heroRight.classList.add('unveiled');
}, 500);

setTimeout(() => {
  if (heroIntro) heroIntro.classList.add('revealed');
}, 1300);

setTimeout(() => {
  if (dividerLine) dividerLine.classList.add('revealed');
}, 1500);

setTimeout(() => {
  if (heroBody) heroBody.classList.add('revealed');
}, 1600);

// Photo background animations
const photoElements = document.querySelectorAll('.approach-photo-bg-img, .hero-left-img, .wwd-photo-img');
photoElements.forEach(img => {
  img.classList.add('loaded');
});

// Approach section animations
const approachCards = document.querySelectorAll('.approach-card');
const approachObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      approachObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

approachCards.forEach(card => {
  approachObserver.observe(card);
});

// Section label animations
const sectionLabels = document.querySelectorAll('.wwd-section-label, .approach-over-label, .enq-label');
const labelObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('in-view');
      labelObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

sectionLabels.forEach(label => {
  labelObserver.observe(label);
});

// What We Do heading animations
const wfdLines = document.querySelectorAll('.wwd-heading .wwd-line');
const wfdObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.parentElement.classList.add('in-view');
      wfdObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

wfdLines.forEach(line => {
  wfdObserver.observe(line);
});

// Enquiries section heading animations
const enquiriesLines = document.querySelectorAll('.enquiries-heading .enq-line');
const enquiriesObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.parentElement.parentElement.classList.add('in-view');
      enquiriesObserver.unobserve(entry.target);
    }
  });
}, observerOptions);

enquiriesLines.forEach(line => {
  enquiriesObserver.observe(line);
});

// Smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href !== '#') {
      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    }
  });
});

console.log('Grissom site loaded successfully');
