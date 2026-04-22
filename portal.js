/**
 * O-PORTAL — Cinematic depth-tunnel scroll animation
 * 
 * Phase 1 (0–40%): Depth lines emerge from the void — scale up from tiny,
 *                   blur fades away, colour fades in, one by one.
 * Phase 2 (40–70%): Hero line (Tm OAK) fully arrives and holds centre stage.
 * Phase 3 (70–85%): The "O" expands like a portal swallowing the screen.
 * Phase 4 (85–100%): White new world is revealed with content fading in.
 */

(function () {
  'use strict';

  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('[portal.js] GSAP / ScrollTrigger not loaded');
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  /* ── DOM refs ──────────────────────────────────────────────── */
  const section     = document.getElementById('o-portal-section');
  const stage       = document.getElementById('o-portal-stage');
  const depthLines  = gsap.utils.toArray('.depth-line');
  const maskWrapper = document.getElementById('o-mask-wrapper');
  const maskGroup   = document.getElementById('o-mask-group');
  const orbitText   = document.getElementById('orbit-text');
  const revealed    = document.getElementById('portal-revealed');
  const revInner    = revealed.querySelector('.portal-revealed-inner');
  const portalO     = document.getElementById('portal-o');

  if (!section) return;

  // Fully dynamic vanilla JS implementation of circular text perfectly synchronized to the circle radius!
  if (orbitText) {
    const textStr = "BEYOND LIMITS • OUR VENTURES • ";
    const chars = textStr.split('');
    const len = chars.length;
    chars.forEach((char, i) => {
      const span = document.createElement('span');
      span.className = 'orbit-char';
      span.innerText = char === ' ' ? '\u00A0' : char;
      
      // Radius of the circle is 100px (200px diameter base). 
      // A translateY of -125px locks each letter mathematically flush to the circumference.
      span.style.transform = `rotate(${i * (360 / len)}deg) translateY(-125px)`;
      orbitText.appendChild(span);
    });
  }

  /* ── Master timeline scrubbed by scroll ────────────────────── */
  const tl = gsap.timeline({ paused: true });

  /* ─────────────────────────────────────────
     PHASE 1: Lines fly in from the distance
     Each line animates 0%–35% of total,
     staggered so they arrive one by one.
  ───────────────────────────────────────── */
  const lineCount = depthLines.length;

  depthLines.forEach((line, i) => {
    const isHero  = line.classList.contains('depth-line--hero');
    const start   = (i / lineCount) * 0.32;
    const arrive  = start + 0.12;
    const hold    = isHero ? 0.72 : arrive + 0.04;

    tl.to(line, {
      opacity: isHero ? 1 : 0.85,
      scale: isHero ? 1 : 0.95,
      color: '#ffffff',
      duration: 0.14,
      ease: 'power2.out',
      force3D: true,
    }, start);

    if (!isHero) {
      tl.to(line, {
        opacity: 0,
        scale: 1.4,
        duration: 0.08,
        ease: 'power2.in',
        force3D: true,
      }, hold);
    }
  });

  /* ─────────────────────────────────────────
     PHASE 2: Hero line holds — nothing to do,
     it's already visible from Phase 1.
  ───────────────────────────────────────── */

  /* ─────────────────────────────────────────
     PHASE 3: O expands → portal flash
     0.70 → 0.85 in normalised timeline
  ───────────────────────────────────────── */

  // Show the mask wrapper
  tl.to(maskWrapper, {
    opacity: 1,
    duration: 0.001,
  }, 0.38);

  // Clamp the group (circle + orbital text) to exactly synchronized scaling
  // Base circle is 200px. Scale x20 gives a 4000px circle which covers any screen.
  tl.fromTo(maskGroup, {
    scale: 0,
    opacity: 1,
  }, {
    scale: 20,
    opacity: 1,
    ease: 'power3.in',
    duration: 0.15,
  }, 0.38);

  // Fade out the depth text hero line as O expands
  tl.to('.depth-line', {
    opacity: 0,
    scale: 1.8,
    duration: 0.08,
    ease: 'power2.in',
    force3D: true,
  }, 0.40);

  /* ─────────────────────────────────────────
     PHASE 4: White world revealed
     0.82 → 1.00
  ───────────────────────────────────────── */
  tl.to(revealed, {
    opacity: 1,
    pointerEvents: 'auto',
    duration: 0.08,
    ease: 'power2.out',
  }, 0.50);

  tl.to(revInner, {
    y: 0,
    opacity: 1,
    duration: 0.12,
    ease: 'power2.out',
  }, 0.53);

  /* ─────────────────────────────────────────
     PHASE 5: Ventures Card Stack
     0.88 → 1.00
  ───────────────────────────────────────── */
  const cards = gsap.utils.toArray('.venture-card');
  const cardCount = cards.length;
  const cardStep = 0.12 / cardCount; // Use the remaining 12% for cards

  // Set initial stack state (staggered in bottom-right)
  cards.forEach((card, i) => {
    gsap.set(card, {
        x: '150%',
        y: '150%',
        rotate: 15,
        opacity: 0,
        scale: 0.9,
    });
  });

  cards.forEach((card, i) => {
    const cardStart = 0.55 + (i * cardStep);
    const stepX = 80;
    const horizontalOffset = (i - 6) * stepX;

    tl.to(card, {
        opacity: 1,
        x: horizontalOffset,
        y: 0,
        rotate: 0,
        scale: 1,
        zIndex: 100 + i,
        duration: cardStep * 3,
        ease: 'power2.out',
        force3D: true,
        immediateRender: false,
    }, cardStart);
  });

  /* ── ScrollTrigger scrubs the timeline ─────────────────────── */
  ScrollTrigger.create({
    trigger: section,
    start: 'top top',
    end: 'bottom bottom',
    scrub: 1.5,
    onUpdate: (self) => {
      tl.progress(self.progress);
    },
  });

})();
