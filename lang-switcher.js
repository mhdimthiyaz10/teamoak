document.addEventListener('DOMContentLoaded', () => {
    const langSwitchers = document.querySelectorAll('.premium-lang-switcher');
    
    // The previous implementation uses 'preferredLang'
    const savedLang = localStorage.getItem('preferredLang') || 'en';
    
    // Initial UI state setup
    updateSwitcherUI(savedLang);
    
    // Initial application of HTML attributes
    applyLanguage(savedLang, false); // false to not trigger Google Translate immediately, we'll do it on window load

    langSwitchers.forEach(switcher => {
        const btn = switcher.querySelector('.pls-btn');
        const options = switcher.querySelectorAll('.pls-option');

        // Toggle dropdown
        btn.addEventListener('click', (e) => {
            e.stopPropagation();
            const expanded = btn.getAttribute('aria-expanded') === 'true';
            
            // Close all other dropdowns
            document.querySelectorAll('.pls-btn').forEach(b => b.setAttribute('aria-expanded', 'false'));
            
            btn.setAttribute('aria-expanded', !expanded);
        });

        // Handle clicks outside
        document.addEventListener('click', (e) => {
            if (!switcher.contains(e.target)) {
                btn.setAttribute('aria-expanded', 'false');
            }
        });

        // Handle language selection
        options.forEach(option => {
            option.addEventListener('click', (e) => {
                e.stopPropagation();
                const lang = option.getAttribute('data-lang');
                
                applyLanguage(lang, true);
                
                updateSwitcherUI(lang);
                btn.setAttribute('aria-expanded', 'false');
            });
        });
    });

    function updateSwitcherUI(lang) {
        document.querySelectorAll('.premium-lang-switcher').forEach(switcher => {
            const btnCurrent = switcher.querySelector('.pls-current');
            const options = switcher.querySelectorAll('.pls-option');
            
            // Update button text
            btnCurrent.textContent = lang === 'ar' ? 'العربية' : 'EN';
            
            // Update active state
            options.forEach(opt => {
                if(opt.getAttribute('data-lang') === lang) {
                    opt.classList.add('active');
                } else {
                    opt.classList.remove('active');
                }
            });
        });
    }

    function applyLanguage(lang, triggerGoogle = true) {
        localStorage.setItem('preferredLang', lang);
        document.documentElement.lang = lang;
        document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
        
        if (triggerGoogle && typeof window.setLanguage === 'function') {
            window.setLanguage(lang);
        }
    }
});

// Sync Google Translate on full page load
window.addEventListener('load', function() {
    setTimeout(function() {
        const savedLang = localStorage.getItem('preferredLang');
        if (savedLang && typeof window.setLanguage === 'function') {
            window.setLanguage(savedLang);
        }
    }, 1000); 
});
