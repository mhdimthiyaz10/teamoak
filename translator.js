(function() {
    const lang = localStorage.getItem('preferredLang') || 'en';
    
    // Hide page immediately if Arabic to avoid FOUT (Flash of Untranslated Text)
    if (lang === 'ar') {
        document.documentElement.style.visibility = 'hidden';
    }
    
    let translations = {};

    async function init() {
        try {
            // Fetch translations
            const [enRes, arRes] = await Promise.all([
                fetch('en.json').then(res => res.json()),
                fetch('ar.json').then(res => res.json())
            ]);
            translations = { en: enRes, ar: arRes };
            
            // Translate page
            translatePage(lang);
            
            // Bind switchers
            setupSwitchers();
        } catch (e) {
            console.error('Failed to load translations:', e);
        } finally {
            // Always show document
            document.documentElement.style.visibility = '';
        }
    }

    function translatePage(currentLang) {
        document.documentElement.lang = currentLang;
        document.documentElement.dir = currentLang === 'ar' ? 'rtl' : 'ltr';
        
        // Translate elements with [data-i18n]
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[currentLang] && translations[currentLang][key]) {
                el.innerHTML = translations[currentLang][key];
            }
        });

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

    // Run when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
