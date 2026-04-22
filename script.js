document.addEventListener('DOMContentLoaded', () => {

    // ── Navbar scroll effect (throttled via rAF) ──────────────
    const navbar = document.getElementById('navbar');
    if (navbar) {
        let ticking = false;
        window.addEventListener('scroll', () => {
            if (!ticking) {
                requestAnimationFrame(() => {
                    navbar.classList.toggle('scrolled', window.scrollY > 50);
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    }

    // ── Fade-in / fade-up animation observer ─────────────────
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) entry.target.classList.add('visible');
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-up, .fade-in').forEach(el => observer.observe(el));

    // ── Scroll-Driven Line Animation ─────────────────────────
    // Uses rAF loop for lerp, but only calls getPointAtLength when truly needed.
    const linePath     = document.getElementById('scroll-line-path');
    const linePoint    = document.getElementById('scroll-line-point');
    const aboutSection = document.getElementById('about');

    if (!linePath || !aboutSection) return;

    const totalLength = linePath.getTotalLength();
    linePath.style.strokeDasharray  = totalLength;
    linePath.style.strokeDashoffset = totalLength;

    let currentOffset = totalLength;
    let targetOffset  = totalLength;
    let lastOffset    = -1;
    let rafId;

    function tick() {
        rafId = requestAnimationFrame(tick);

        currentOffset += (targetOffset - currentOffset) * 0.07;
        if (Math.abs(currentOffset - targetOffset) < 0.2) currentOffset = targetOffset;

        // Skip DOM writes if nothing changed meaningfully
        if (Math.abs(currentOffset - lastOffset) < 0.1) return;
        lastOffset = currentOffset;

        linePath.style.strokeDashoffset = currentOffset;

        const drawnLength = totalLength - currentOffset;
        if (drawnLength > 1) {
            const point = linePath.getPointAtLength(drawnLength);
            linePoint.setAttribute('cx', point.x);
            linePoint.setAttribute('cy', point.y);
            linePoint.classList.add('visible');
        } else {
            linePoint.classList.remove('visible');
        }
    }
    tick();

    let scrollTick = false;
    function updateLine() {
        if (scrollTick) return;
        scrollTick = true;
        requestAnimationFrame(() => {
            const scrollY       = window.scrollY;
            const vh            = window.innerHeight;
            const sectionTop    = aboutSection.offsetTop;
            const sectionHeight = aboutSection.offsetHeight;
            const drawStart     = sectionTop - vh * 0.8;
            const drawEnd       = sectionTop + sectionHeight - vh * 0.2;
            const progress      = Math.min(Math.max((scrollY - drawStart) / Math.max(drawEnd - drawStart, 1), 0), 1);
            targetOffset        = totalLength * (1 - progress);
            scrollTick = false;
        });
    }

    window.addEventListener('scroll', updateLine, { passive: true });
    window.addEventListener('resize', updateLine, { passive: true });
    updateLine();


    // ── Scroll Reveal (opacity only — no blur for perf) ──────
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        document.querySelectorAll('.scroll-reveal-container').forEach(container => {
            const textElements = container.querySelectorAll('.scroll-reveal-text');

            textElements.forEach(el => {
                const words = el.innerText.split(/(\s+)/).map(word =>
                    word.match(/^\s+$/) ? word : `<span class="word">${word}</span>`
                );
                el.innerHTML = words.join('');
            });

            const wordElements = container.querySelectorAll('.word');

            // Subtle container tilt
            gsap.fromTo(container,
                { transformOrigin: '0% 50%', rotate: 2 },
                {
                    rotate: 0,
                    ease: 'none',
                    scrollTrigger: {
                        trigger: container,
                        start: 'top bottom',
                        end: 'bottom bottom',
                        scrub: 1,
                    }
                }
            );

            // Opacity only — no filter:blur (massive perf win)
            gsap.fromTo(wordElements,
                { opacity: 0.08, willChange: 'opacity' },
                {
                    opacity: 1,
                    ease: 'none',
                    stagger: 0.04,
                    willChange: 'opacity',
                    scrollTrigger: {
                        trigger: container,
                        start: 'top bottom-=15%',
                        end: 'bottom bottom',
                        scrub: 1,
                    }
                }
            );
        });
    }
});
