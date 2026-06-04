document.addEventListener('DOMContentLoaded', () => {
  const year = document.getElementById('current-year');
  if (year) year.textContent = new Date().getFullYear();

  document.querySelectorAll('a[href^="#"]').forEach((link) => {
    link.addEventListener('click', (event) => {
      const target = document.querySelector(link.getAttribute('href'));
      if (target) {
        event.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Handle contact form submission
  const contactForm = document.getElementById('contact-form-index');
  if (contactForm) {
    contactForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      
      const formData = {
        name: document.getElementById('name').value,
        email: document.getElementById('email').value,
        company: document.getElementById('company').value,
        subject: document.getElementById('subject').value,
        message: document.getElementById('message').value
      };

      try {
        const response = await fetch('/api/contact', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(formData)
        });

        const data = await response.json();

        if (data.status === 'success') {
          contactForm.reset();
          alert('Thank you for your enquiry! We will be in touch soon.');
        } else {
          alert(data.message || 'An error occurred. Please try again.');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('An error occurred. Please try again later.');
      }
    });
  }

  // Scroll animation observer
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('[data-animate], [data-stagger], .stats-bar').forEach(el => {
    observer.observe(el);
  });
});