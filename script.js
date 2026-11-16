(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* footer year */
  document.querySelectorAll('[data-year]').forEach(n => (n.textContent = new Date().getFullYear()));

  /* mobile menu */
  const toggle = document.querySelector('.nav__toggle');
  const menu = document.getElementById('menu');
  if (toggle && menu) {
    const set = open => {
      toggle.setAttribute('aria-expanded', open);
      toggle.querySelector('b').textContent = open ? 'Close' : 'Menu';
      menu.hidden = !open;
      document.body.style.overflow = open ? 'hidden' : '';
    };
    toggle.addEventListener('click', () => set(menu.hidden));
    menu.addEventListener('click', e => e.target.closest('a') && set(false));
    addEventListener('keydown', e => e.key === 'Escape' && !menu.hidden && set(false));
    matchMedia('(min-width: 761px)').addEventListener('change', e => e.matches && set(false));
  }

  /* nav hides on scroll down, returns on scroll up */
  const nav = document.getElementById('nav');
  let lastY = scrollY;
  addEventListener('scroll', () => {
    const y = scrollY;
    if (menu && !menu.hidden) return;
    nav.classList.toggle('is-hidden', y > lastY && y > 400);
    lastY = y;
  }, { passive: true });

  /* count-up */
  const count = el => {
    const end = +el.dataset.count;
    if (reduce || !end) return;
    const t0 = performance.now(), dur = 1100;
    const step = t => {
      const p = Math.min(1, (t - t0) / dur);
      el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3)));
      if (p < 1) requestAnimationFrame(step);
    };
    el.textContent = 0;
    requestAnimationFrame(step);
  };

  /* reveal on scroll, staggered among siblings */
  const rv = [...document.querySelectorAll('.rv')];
  if (!('IntersectionObserver' in window) || reduce) {
    rv.forEach(el => el.classList.add('in'));
  } else {
    const show = (el, i) => {
      el.style.transitionDelay = Math.min(i, 8) * 70 + 'ms';
      el.classList.add('in');
      el.addEventListener('transitionend', () => (el.style.transitionDelay = ''), { once: true });
      const n = el.querySelector('[data-count]');
      if (n) setTimeout(() => count(n), Math.min(i, 8) * 70);
    };
    const io = new IntersectionObserver(entries => {
      entries.filter(e => e.isIntersecting).forEach((e, i) => { show(e.target, i); io.unobserve(e.target); });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    /* anything already on screen at load is revealed straight away, the rest on scroll */
    const above = [];
    rv.forEach(el => {
      const r = el.getBoundingClientRect();
      if (r.top < innerHeight * 0.92 && r.bottom > 0) above.push(el); else io.observe(el);
    });
    setTimeout(() => above.forEach(show), 60);
  }

  /* hero chart: a live line that keeps climbing from "ambition" to "offers" */
  const canvas = document.getElementById('chart');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    const css = getComputedStyle(document.documentElement);
    const ACID = css.getPropertyValue('--acid').trim() || '#d6ff3f';
    const N = 120;
    let seed = 11;
    const rnd = () => ((seed = (seed * 1664525 + 1013904223) >>> 0) / 4294967296);
    const next = v => v + (rnd() - 0.33) * 1.0 + (rnd() < 0.06 ? -1.2 : 0);
    const vals = [0];
    for (let i = 1; i < N; i++) vals.push(next(vals[i - 1]));
    let lo = Math.min(...vals), hi = Math.max(...vals);
    let w = 0, h = 0, kTop = 0, intro = reduce ? 1 : 0, slide = 0, visible = true, raf = 0, last = 0;

    const size = () => {
      const dpr = Math.min(devicePixelRatio || 1, 2);
      w = canvas.clientWidth; h = canvas.clientHeight;
      canvas.width = w * dpr; canvas.height = h * dpr;
      const k = document.querySelector('.hero .kicker');
      kTop = k ? k.getBoundingClientRect().top - canvas.getBoundingClientRect().top : h * 0.4;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };

    const draw = () => {
      ctx.clearRect(0, 0, w, h);
      const small = w < 700;
      const g = small ? 56 : 88;
      ctx.lineWidth = 1;
      ctx.strokeStyle = 'rgba(239,236,228,.055)';
      ctx.beginPath();
      for (let x = w % g; x < w; x += g) { ctx.moveTo(x + .5, 0); ctx.lineTo(x + .5, h); }
      for (let y = g; y < h; y += g) { ctx.moveTo(0, y + .5); ctx.lineTo(w, y + .5); }
      ctx.stroke();

      const right = w - (small ? 74 : 132);
      /* on small screens the line stays above the hero text, however short the screen is */
      const bot = small ? Math.min(h * 0.33, kTop - 14) : h * 0.7;
      const top = small ? Math.max(0, Math.min(h * 0.13, bot - 40)) : h * 0.17;
      const stepX = right / (N - 2);
      const X = i => (i - slide) * stepX;
      const Y = v => bot - ((v - lo) / (hi - lo || 1)) * (bot - top);
      const shown = Math.max(1, intro * (N - 1));
      const full = Math.floor(shown), frac = shown - full;

      const pts = [];
      for (let i = 0; i <= full && i < N; i++) pts.push([X(i), Y(vals[i])]);
      if (full < N - 1) {
        pts.push([X(full) + stepX * frac, Y(vals[full] + (vals[full + 1] - vals[full]) * frac)]);
      } else {
        const a = pts[pts.length - 2], b = pts[pts.length - 1];
        pts[pts.length - 1] = [a[0] + (b[0] - a[0]) * (1 - slide), a[1] + (b[1] - a[1]) * (1 - slide)];
        if (slide === 0) pts[pts.length - 1] = b;
      }
      const [hx, hy] = pts[pts.length - 1];

      const area = ctx.createLinearGradient(0, top, 0, bot + (bot - top) * (small ? 0.35 : 0.3));
      area.addColorStop(0, 'rgba(214,255,63,.16)');
      area.addColorStop(1, 'rgba(214,255,63,0)');
      ctx.beginPath();
      pts.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)));
      ctx.lineTo(hx, h); ctx.lineTo(pts[0][0], h); ctx.closePath();
      ctx.fillStyle = area; ctx.fill();

      const stroke = ctx.createLinearGradient(0, 0, right, 0);
      stroke.addColorStop(0, 'rgba(214,255,63,.12)');
      stroke.addColorStop(.55, 'rgba(214,255,63,.75)');
      stroke.addColorStop(1, ACID);
      ctx.beginPath();
      pts.forEach(([x, y], i) => (i ? ctx.lineTo(x, y) : ctx.moveTo(x, y)));
      ctx.strokeStyle = stroke; ctx.lineWidth = small ? 1.6 : 2; ctx.lineJoin = 'round'; ctx.stroke();

      /* price line + tag */
      ctx.setLineDash([3, 5]);
      ctx.strokeStyle = 'rgba(214,255,63,.4)'; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(hx, hy + .5); ctx.lineTo(w, hy + .5); ctx.stroke();
      ctx.setLineDash([]);
      const pulse = reduce ? 0 : (performance.now() % 1800) / 1800;
      ctx.beginPath(); ctx.arc(hx, hy, 5 + pulse * 14, 0, 7);
      ctx.fillStyle = `rgba(214,255,63,${0.28 * (1 - pulse)})`; ctx.fill();
      ctx.beginPath(); ctx.arc(hx, hy, 4.5, 0, 7); ctx.fillStyle = ACID; ctx.fill();

      const label = intro < 1 ? 'AMBITION' : 'OFFERS ▲';
      ctx.font = `500 ${small ? 10 : 11.5}px "Geist Mono", ui-monospace, monospace`;
      const tw = ctx.measureText(label).width + 16, th = small ? 20 : 24;
      const tx = Math.min(w - tw - 6, hx + 16), ty = hy - th / 2;
      ctx.fillStyle = ACID;
      ctx.beginPath();
      if (ctx.roundRect) ctx.roundRect(tx, ty, tw, th, 5); else ctx.rect(tx, ty, tw, th);
      ctx.fill();
      ctx.fillStyle = '#0d0e12'; ctx.textBaseline = 'middle';
      ctx.fillText(label, tx + 8, ty + th / 2 + 1);
    };

    const frame = t => {
      raf = 0;
      const dt = Math.min(50, t - (last || t)); last = t;
      if (intro < 1) {
        intro = Math.min(1, intro + dt / 2600 * (1.35 - intro));
        if (intro > 0.999) intro = 1;
      } else {
        slide += dt / 1100;
        if (slide >= 1) { slide -= 1; vals.push(next(vals[vals.length - 1])); vals.shift(); }
        const mn = Math.min(...vals), mx = Math.max(...vals);
        lo += (mn - lo) * 0.04; hi += (mx - hi) * 0.04;
      }
      draw();
      if (visible && !reduce) raf = requestAnimationFrame(frame);
    };
    const kick = () => { if (!raf && !reduce) { last = 0; raf = requestAnimationFrame(frame); } };

    size(); draw();
    addEventListener('resize', () => { size(); draw(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([e]) => { visible = e.isIntersecting; if (visible) kick(); }).observe(canvas);
    }
    document.addEventListener('visibilitychange', () => { visible = !document.hidden; if (visible) kick(); });
    (document.fonts ? document.fonts.ready : Promise.resolve()).then(() => { draw(); kick(); });
  }
})();
