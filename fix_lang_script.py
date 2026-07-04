import glob
import re

JS_CONTENT = """document.addEventListener('DOMContentLoaded', () => {
    const langSwitchers = document.querySelectorAll('.premium-lang-switcher');
    
    // The previous implementation uses 'preferredLang'
    const savedLang = localStorage.getItem('preferredLang') || 'en';
    
    // Initial UI state setup
    updateSwitcherUI(savedLang);

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
                
                // Trigger Google Translate via existing global function
                if (typeof window.setLanguage === 'function') {
                    window.setLanguage(lang);
                } else {
                    applyLanguage(lang);
                }
                
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

    function applyLanguage(lang) {
        localStorage.setItem('preferredLang', lang);
        document.documentElement.lang = lang;
        document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
    }
});
"""

def main():
    # Write updated JS
    with open('lang-switcher.js', 'w', encoding='utf-8') as f:
        f.write(JS_CONTENT)
        
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Fix the literal \\n
        if '\\\\n</body>' in content:
            content = content.replace('\\\\n</body>', '\\n</body>')
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {file}")

if __name__ == '__main__':
    main()
