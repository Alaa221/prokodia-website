// ══════════════════════════════════════════════
//   PROKODIA — Main JavaScript
// ══════════════════════════════════════════════

// Navbar scroll effect
const navbar = document.getElementById('navbar');
window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 40);
});

// Mobile menu toggle
const menuToggle = document.getElementById('menuToggle');
const navLinks = document.querySelector('.nav-links');
menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('open');
  menuToggle.textContent = navLinks.classList.contains('open') ? '✕' : '☰';
});
navLinks.querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    navLinks.classList.remove('open');
    menuToggle.textContent = '☰';
  });
});

// Fade-up on scroll
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) e.target.classList.add('visible');
  });
}, { threshold: 0.12 });

document.querySelectorAll(
  '.service-card, .project-card, .stat-card, .why-text, .why-visual, .contact-form, .section-header'
).forEach((el, i) => {
  el.classList.add('fade-up');
  el.style.transitionDelay = (i % 4) * 0.1 + 's';
  observer.observe(el);
});

// Contact form submit
const form = document.querySelector('.contact-form');
if (form) {
  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const btn = form.querySelector('button[type=submit]');
    btn.textContent = '✓ تم الإرسال! هنتواصل معاك قريباً';
    btn.style.background = 'linear-gradient(135deg,#059669,#10b981)';
    btn.style.boxShadow = '0 4px 30px rgba(16,185,129,0.4)';
    btn.disabled = true;
  });
}
