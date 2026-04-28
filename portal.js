(function () {
  'use strict';

  if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
    console.warn('[portal.js] GSAP / ScrollTrigger not loaded');
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  const section = document.getElementById('building-excellence');
  const track = document.querySelector('.excellence-track');

  if (!section || !track) return;

  // Optimize performance by enforcing hardware acceleration
  gsap.set(track, { willChange: 'transform', force3D: true });

  // Calculate the amount to scroll horizontally
  function getScrollAmount() {
    let trackWidth = track.scrollWidth;
    return -(trackWidth - window.innerWidth + (window.innerWidth * 0.15)); // Calculate distance
  }

  // Create the horizontal scroll animation
  const tween = gsap.to(track, {
    x: getScrollAmount,
    ease: "none",
    force3D: true
  });

  ScrollTrigger.create({
    trigger: section,
    start: "top top",
    end: () => `+=${track.scrollWidth}`, // Scrolling distance based on track length
    pin: true,
    animation: tween,
    scrub: 0.5, // Reduced scrub for less input lag but still smooth
    invalidateOnRefresh: true, 
    anticipatePin: 1 // Prevents visual jumps right before pinning
  });

  // Ensure scroll height calculations are correct after images load
  window.addEventListener('load', () => {
    ScrollTrigger.refresh();
  });

  // --- Interactive Map Pins Animation ---
  const mapPins = document.querySelectorAll('.map-pin');
  if (mapPins.length > 0) {
    // Animate map pins popping in
    gsap.from('.map-pin', {
      scale: 0,
      opacity: 0,
      duration: 0.8,
      stagger: 0.15,
      ease: 'back.out(1.7)',
      scrollTrigger: {
        trigger: '.interactive-map-wrapper',
        start: 'top 75%'
      }
    });
  }

})();
