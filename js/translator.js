(function() {
    const lang = localStorage.getItem('preferredLang') || 'en';
    
    // Hide page immediately if Arabic to avoid FOUT (Flash of Untranslated Text)
    if (lang === 'ar') {
        document.documentElement.style.visibility = 'hidden';
    }
    
    let translations = {};

    function checkIsSubpage() {
        const path = window.location.pathname;
        return path.includes('/pages/') || (path.endsWith('.html') && !path.endsWith('index.html'));
    }

    function resolveRelativeHref(href, isSubpage) {
        if (!href || href.startsWith('http://') || href.startsWith('https://') || href.startsWith('javascript:') || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) {
            return href;
        }

        let clean = href.trim();
        if (!isSubpage) {
            // We are on index.html (root directory)
            if (clean === 'index.html' || clean === './index.html' || clean === '/') {
                return 'index.html';
            }
            if (!clean.startsWith('pages/') && !clean.startsWith('./pages/')) {
                clean = clean.replace(/^\.\//, '');
                return 'pages/' + clean;
            }
            return clean;
        } else {
            // We are inside pages/ directory
            if (clean === 'index.html' || clean === './index.html' || clean === '/') {
                return '../index.html';
            }
            if (clean.startsWith('pages/') || clean.startsWith('./pages/')) {
                return clean.replace(/^(\.\/)?pages\//, '');
            }
            return clean;
        }
    }

    function fixContainerLinks(container, isSubpage) {
        if (!container) return;
        container.querySelectorAll('a[href]').forEach(a => {
            const rawHref = a.getAttribute('href');
            const newHref = resolveRelativeHref(rawHref, isSubpage);
            if (newHref && newHref !== rawHref) {
                a.setAttribute('href', newHref);
            }
        });
    }

    async function init() {
        try {
            // Fetch translations
            const isSubpage = checkIsSubpage();
            const localePath = isSubpage ? '../locales/' : 'locales/';
            const [enRes, arRes] = await Promise.all([
                fetch(localePath + 'en.json').then(res => res.json()),
                fetch(localePath + 'ar.json').then(res => res.json())
            ]);
            translations = { en: enRes, ar: arRes };
            
            // Translate page
            translatePage(lang);
            
            // Bind switchers and navigation dropdowns
            setupSwitchers();
            setupNavDropdowns();
        } catch (e) {
            console.error('Failed to load translations:', e);
        } finally {
            // Always show document and ensure navigation is initialized
            document.documentElement.style.visibility = '';
            setupNavDropdowns();
        }
    }

    function translatePage(currentLang) {
        const isSubpage = checkIsSubpage();
        document.documentElement.lang = currentLang;
        document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
        
        // Translate elements with [data-i18n]
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[currentLang] && translations[currentLang][key]) {
                el.innerHTML = translations[currentLang][key];
                fixContainerLinks(el, isSubpage);
            }
        });

        // Ensure all page links are correctly prefixed for root vs subpage
        fixContainerLinks(document.body, isSubpage);

        // Translate placeholders
        document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (translations[currentLang] && translations[currentLang][key]) {
                el.setAttribute('placeholder', translations[currentLang][key]);
            }
        });

        // Translate image alts
        document.querySelectorAll('[data-i18n-alt]').forEach(el => {
            const key = el.getAttribute('data-i18n-alt');
            if (translations[currentLang] && translations[currentLang][key]) {
                el.setAttribute('alt', translations[currentLang][key]);
            }
        });

        // Translate title
        const titleEl = document.querySelector('title[data-i18n]');
        if (titleEl) {
            const key = titleEl.getAttribute('data-i18n');
            if (translations[currentLang] && translations[currentLang][key]) {
                document.title = translations[currentLang][key];
            }
        }

        // Translate meta description
        const metaDesc = document.querySelector('meta[name="description"][data-i18n]');
        if (metaDesc) {
            const key = metaDesc.getAttribute('data-i18n');
            if (translations[currentLang] && translations[currentLang][key]) {
                metaDesc.setAttribute('content', translations[currentLang][key]);
            }
        }

        // Update switcher buttons UI
        updateSwitcherUI(currentLang);
        
        // Dispatch event for any custom components that need to re-render in RTL (like sliders)
        window.dispatchEvent(new CustomEvent('languagechange', { detail: { lang: currentLang } }));
    }

    function setupSwitchers() {
        document.querySelectorAll('.premium-lang-switcher').forEach(switcher => {
            const btn = switcher.querySelector('.pls-btn');
            const dropdown = switcher.querySelector('.pls-dropdown');
            
            if (!btn) return;
            
            // Toggle dropdown on button click
            btn.addEventListener('click', (e) => {
                e.stopPropagation();
                const isExpanded = btn.getAttribute('aria-expanded') === 'true';
                
                // Close all other switchers first
                document.querySelectorAll('.pls-btn').forEach(b => b.setAttribute('aria-expanded', 'false'));
                
                btn.setAttribute('aria-expanded', !isExpanded ? 'true' : 'false');
            });

            // Handle option selection
            switcher.querySelectorAll('.pls-option').forEach(option => {
                option.addEventListener('click', () => {
                    const newLang = option.getAttribute('data-lang');
                    localStorage.setItem('preferredLang', newLang);
                    translatePage(newLang);
                    
                    // Close dropdown
                    btn.setAttribute('aria-expanded', 'false');
                });
            });
        });

        // Close dropdowns on click outside
        document.addEventListener('click', () => {
            document.querySelectorAll('.pls-btn').forEach(b => b.setAttribute('aria-expanded', 'false'));
        });
    }

    function updateSwitcherUI(currentLang) {
        document.querySelectorAll('.premium-lang-switcher').forEach(switcher => {
            const btn = switcher.querySelector('.pls-btn');
            const currentLabel = switcher.querySelector('.pls-current');
            
            if (currentLabel) {
                currentLabel.textContent = currentLang.toUpperCase();
            }

            switcher.querySelectorAll('.pls-option').forEach(option => {
                if (option.getAttribute('data-lang') === currentLang) {
                    option.classList.add('active');
                } else {
                    option.classList.remove('active');
                }
            });
        });
    }

    function setupNavDropdowns() {
        // Main dropdown toggle on click for "What We Do" (.has-arrow)
        document.querySelectorAll('.has-arrow').forEach(li => {
            const trigger = li.querySelector(':scope > a');
            if (!trigger || trigger.dataset.navBound === 'true') return;
            trigger.dataset.navBound = 'true';

            trigger.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const isOpen = li.classList.contains('open');

                // Close all other open top-level dropdowns
                document.querySelectorAll('.has-arrow.open').forEach(otherLi => {
                    if (otherLi !== li) {
                        otherLi.classList.remove('open');
                        otherLi.querySelectorAll('.has-flyout.open, .has-flyout.active').forEach(f => {
                            f.classList.remove('open', 'active');
                        });
                    }
                });

                if (isOpen) {
                    li.classList.remove('open');
                    li.querySelectorAll('.has-flyout.open, .has-flyout.active').forEach(f => {
                        f.classList.remove('open', 'active');
                    });
                } else {
                    li.classList.add('open');
                    // On desktop, activate first flyout item by default
                    if (window.innerWidth > 768) {
                        const firstFlyout = li.querySelector('.dropdown > li.has-flyout');
                        if (firstFlyout) {
                            firstFlyout.classList.add('active');
                        }
                    }
                }
            });
        });

        // Flyout categories (Trading, Services, Industrial)
        document.querySelectorAll('.dropdown > li.has-flyout').forEach(flyoutLi => {
            const flyoutTrigger = flyoutLi.querySelector(':scope > a');

            // Mouse enter switches active flyout on desktop only
            flyoutLi.addEventListener('mouseenter', () => {
                if (window.innerWidth > 768) {
                    const siblings = flyoutLi.parentElement.querySelectorAll(':scope > li.has-flyout');
                    siblings.forEach(s => s.classList.remove('active', 'open'));
                    flyoutLi.classList.add('active');
                }
            });

            if (flyoutTrigger && flyoutTrigger.dataset.flyoutBound !== 'true') {
                flyoutTrigger.dataset.flyoutBound = 'true';
                flyoutTrigger.addEventListener('click', (e) => {
                    e.preventDefault();
                    e.stopPropagation();
                    const isFlyoutOpen = flyoutLi.classList.contains('open');
                    const siblings = flyoutLi.parentElement.querySelectorAll(':scope > li.has-flyout');
                    siblings.forEach(s => {
                        if (s !== flyoutLi) s.classList.remove('open', 'active');
                    });

                    if (isFlyoutOpen) {
                        flyoutLi.classList.remove('open', 'active');
                    } else {
                        flyoutLi.classList.add('open', 'active');
                    }
                });
            }
        });

        // Close dropdowns on outside click
        if (!window._oakNavGlobalBound) {
            window._oakNavGlobalBound = true;
            document.addEventListener('click', (e) => {
                if (!e.target.closest('.has-arrow') && !e.target.closest('.has-flyout')) {
                    document.querySelectorAll('.has-arrow.open').forEach(el => {
                        el.classList.remove('open');
                        el.querySelectorAll('.has-flyout.open, .has-flyout.active').forEach(f => {
                            f.classList.remove('open', 'active');
                        });
                    });
                }
            });

            // Close on Escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    document.querySelectorAll('.has-arrow.open').forEach(el => {
                        el.classList.remove('open');
                        el.querySelectorAll('.has-flyout.open, .has-flyout.active').forEach(f => {
                            f.classList.remove('open', 'active');
                        });
                    });
                }
            });
        }
    }

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
