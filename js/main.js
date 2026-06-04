// ===== PARTICLE NETWORK =====
(function () {
  const canvas = document.getElementById('particle-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  let W, H, particles;
  const COUNT = 60, MAX_DIST = 130;

  function resize() {
    W = canvas.width  = canvas.offsetWidth;
    H = canvas.height = canvas.offsetHeight;
  }

  function rand(min, max) { return Math.random() * (max - min) + min; }

  function initParticles() {
    particles = Array.from({ length: COUNT }, () => ({
      x: rand(0, W), y: rand(0, H),
      vx: rand(-0.4, 0.4), vy: rand(-0.4, 0.4),
      r: rand(1.5, 3)
    }));
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > W) p.vx *= -1;
      if (p.y < 0 || p.y > H) p.vy *= -1;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255,255,255,0.7)';
      ctx.fill();
    });
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < MAX_DIST) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = `rgba(255,255,255,${0.35 * (1 - dist / MAX_DIST)})`;
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', () => { resize(); initParticles(); });
  resize();
  initParticles();
  draw();
})();

// ===== TYPING EFFECT =====
(function () {
  const el = document.getElementById('typing-text');
  if (!el) return;
  const texts = ['데이터 분석가', '개발자', 'Data Analyst'];
  let ti = 0, ci = 0, deleting = false;

  function type() {
    const current = texts[ti];
    el.textContent = deleting ? current.slice(0, ci--) : current.slice(0, ci++);
    if (!deleting && ci > current.length) {
      deleting = true;
      setTimeout(type, 1500);
      return;
    }
    if (deleting && ci < 0) {
      deleting = false;
      ti = (ti + 1) % texts.length;
      ci = 0;
      setTimeout(type, 400);
      return;
    }
    setTimeout(type, deleting ? 60 : 100);
  }

  setTimeout(type, 600);
})();

// ===== ACTIVE NAV LINK HIGHLIGHT ON SCROLL =====
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
