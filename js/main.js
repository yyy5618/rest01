// Active nav link highlight on scroll
const sections = document.querySelectorAll('main section[id]');
const navLinks = document.querySelectorAll('#navbar a');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(a => a.classList.remove('active'));
      const active = document.querySelector(`#navbar a[href="#${entry.target.id}"]`);
      if (active) active.classList.add('active');
    }
  });
}, { rootMargin: '-50% 0px -45% 0px' });

sections.forEach(s => observer.observe(s));

// Hide broken profile image gracefully
const profileImg = document.getElementById('profile-photo');
if (profileImg) {
  profileImg.addEventListener('error', () => {
    profileImg.style.display = 'none';
  });
}
