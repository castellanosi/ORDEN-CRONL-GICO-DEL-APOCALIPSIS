(() => {
  const button = document.querySelector('#menu');
  const sidebar = document.querySelector('#sidebar');
  const setMenu = open => { sidebar.classList.toggle('open', open); button.setAttribute('aria-expanded', String(open)); };
  button.addEventListener('click', () => setMenu(!sidebar.classList.contains('open')));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && sidebar.classList.contains('open')) { setMenu(false); button.focus(); } });
  document.addEventListener('click', e => { if (!sidebar.contains(e.target) && !button.contains(e.target)) setMenu(false); });
  sidebar.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  const size = document.querySelector('#font-size');
  if (size) { try { const saved = localStorage.getItem('reading-size'); if (['18','20','22'].includes(saved)) size.value = saved; } catch {} const apply = () => document.documentElement.style.setProperty('--reading-size', size.value + 'px'); apply(); size.addEventListener('change', () => { apply(); try { localStorage.setItem('reading-size', size.value); } catch {} }); }
  const headings = [...document.querySelectorAll('.article h2, .article h3')];
  const links = [...document.querySelectorAll('.toc a')];
  if (headings.length) {
    let queued = false;
    const update = () => { queued = false; let current = headings[0]; for (const h of headings) { if (h.getBoundingClientRect().top <= 140) current = h; else break; } for (const a of links) { const active = a.hash === '#' + current.id; a.classList.toggle('active', active); if (active) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); } };
    window.addEventListener('scroll', () => { if (!queued) { queued = true; requestAnimationFrame(update); } }, {passive:true}); update();
  }
})();
