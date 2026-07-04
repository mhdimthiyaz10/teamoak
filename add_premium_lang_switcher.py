import os
import glob
import re

CSS_CONTENT = """
/* ═══════════════════════════
   PREMIUM LANGUAGE SWITCHER
═══════════════════════════ */
.premium-lang-switcher {
    position: relative;
    display: inline-flex;
    align-items: center;
    margin-right: 20px;
    z-index: 1000;
    font-family: var(--font-body, 'Plus Jakarta Sans', sans-serif);
}

html[dir="rtl"] .premium-lang-switcher {
    margin-right: 0;
    margin-left: 20px;
}

.pls-btn {
    display: flex;
    align-items: center;
    gap: 6px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 30px;
    padding: 6px 12px;
    color: #ffffff;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    backdrop-filter: blur(10px);
}

.nav .pls-btn {
    background: rgba(0, 0, 0, 0.03);
    border: 1px solid rgba(0, 0, 0, 0.1);
    color: #111111;
}
.hero-navbar .pls-btn {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    color: #ffffff;
}

.pls-btn:hover {
    background: rgba(197, 155, 39, 0.1);
    border-color: #c59b27;
    color: #c59b27;
}

.nav .pls-btn:hover {
    background: rgba(197, 155, 39, 0.1);
}

.pls-globe {
    opacity: 0.8;
}

.pls-arrow {
    opacity: 0.6;
    transition: transform 0.3s ease;
}

.pls-btn[aria-expanded="true"] .pls-arrow {
    transform: rotate(180deg);
}

.pls-btn[aria-expanded="true"] {
    background: rgba(197, 155, 39, 0.1);
    border-color: #c59b27;
    color: #c59b27;
}

.pls-dropdown {
    position: absolute;
    top: calc(100% + 10px);
    right: 0;
    background: #ffffff;
    border-radius: 12px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.1);
    min-width: 150px;
    padding: 8px;
    opacity: 0;
    pointer-events: none;
    transform: translateY(-10px);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border: 1px solid rgba(0,0,0,0.05);
}

html[dir="rtl"] .pls-dropdown {
    right: auto;
    left: 0;
}

.pls-btn[aria-expanded="true"] + .pls-dropdown,
.premium-lang-switcher.active .pls-dropdown {
    opacity: 1;
    pointer-events: all;
    transform: translateY(0);
}

.pls-option {
    display: flex;
    align-items: center;
    gap: 10px;
    width: 100%;
    padding: 10px 12px;
    background: transparent;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    text-align: left;
    transition: all 0.2s ease;
    color: #444444;
}

html[dir="rtl"] .pls-option {
    text-align: right;
}

.pls-code {
    font-size: 0.75rem;
    font-weight: 700;
    color: #888888;
    background: #f0f0f0;
    padding: 2px 6px;
    border-radius: 4px;
    transition: all 0.2s ease;
}

.pls-name {
    font-size: 0.9rem;
    font-weight: 600;
}

.pls-option:hover {
    background: #f9f9f9;
}

.pls-option.active {
    background: rgba(197, 155, 39, 0.08);
    color: #c59b27;
}

.pls-option.active .pls-code {
    background: #c59b27;
    color: #ffffff;
}

/* Base RTL Styles */
html[dir="rtl"] {
    text-align: right;
    direction: rtl;
}

/* Automatically flip margin/padding for standard utility classes if needed, 
   but for now we focus on mirroring the UI components. */
html[dir="rtl"] .hero-nav-container,
html[dir="rtl"] .nav,
html[dir="rtl"] .footer-inner {
    flex-direction: row;
}

html[dir="rtl"] .nav-links {
    padding-right: 0;
}

/* Mega menu dropdown fixes for RTL */
html[dir="rtl"] .nav-links li.has-arrow .dropdown {
    left: auto !important;
    right: 50% !important;
    transform: translateX(50%) translateY(-10px) !important;
}
html[dir="rtl"] .nav-links li.has-arrow.open .dropdown {
    transform: translateX(50%) translateY(0) !important;
}
html[dir="rtl"] .nav-links li.has-arrow .dropdown li.has-flyout .flyout {
    left: auto !important;
    right: calc(100% + 5px) !important;
    transform: translateX(10px) !important;
}
html[dir="rtl"] .nav-links li.has-arrow .dropdown > li.has-flyout:hover .flyout {
    transform: translateX(0) !important;
}
html[dir="rtl"] .mf-contact-item {
    flex-direction: row;
}
html[dir="rtl"] .mf-text {
    padding-top: 5px;
    padding-right: 15px;
    padding-left: 0;
}

/* Mobile Nav Flip */
html[dir="rtl"] .nav-links {
    right: auto !important;
    left: -100%;
    border-left: none;
    border-right: 1px solid rgba(255,255,255,0.05);
    transition: left 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}
html[dir="rtl"] .nav-links.active {
    left: 0;
}
"""

JS_CONTENT = """
document.addEventListener('DOMContentLoaded', () => {
    const langSwitchers = document.querySelectorAll('.premium-lang-switcher');
    
    // Check localStorage
    const savedLang = localStorage.getItem('teamOakLang') || 'en';
    applyLanguage(savedLang, false);

    langSwitchers.forEach(switcher => {
        const btn = switcher.querySelector('.pls-btn');
        const dropdown = switcher.querySelector('.pls-dropdown');
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
                btn.setAttribute('aria-expanded', 'false');
            });
        });
    });

    function applyLanguage(lang, shouldReload = false) {
        localStorage.setItem('teamOakLang', lang);
        
        // Update HTML attributes
        document.documentElement.lang = lang;
        document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';
        
        // Update UI
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
        
        // Optional: Trigger custom event for other scripts
        document.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang } }));
    }
});
"""

HTML_CONTENT = """
<div class="premium-lang-switcher">
    <button class="pls-btn" aria-label="Select Language" aria-expanded="false">
        <svg class="pls-globe" viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
        <span class="pls-current">EN</span>
        <svg class="pls-arrow" viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
    </button>
    <div class="pls-dropdown">
        <button class="pls-option active" data-lang="en">
            <span class="pls-code">EN</span>
            <span class="pls-name">English</span>
        </button>
        <button class="pls-option" data-lang="ar">
            <span class="pls-code">ع</span>
            <span class="pls-name">العربية</span>
        </button>
    </div>
</div>
"""

OLD_HTML_REGEX = re.compile(r'<div class="lang-switcher">.*?</div>', re.DOTALL)
OLD_STYLE_REGEX = re.compile(r'<style>\s*/\*\s*Language Switcher\s*\*/.*?</style>', re.DOTALL)

def main():
    # 1. Update style.css
    with open('style.css', 'r', encoding='utf-8') as f:
        style_content = f.read()
    
    if "PREMIUM LANGUAGE SWITCHER" not in style_content:
        with open('style.css', 'a', encoding='utf-8') as f:
            f.write('\\n' + CSS_CONTENT)
            
    # 2. Create lang-switcher.js
    with open('lang-switcher.js', 'w', encoding='utf-8') as f:
        f.write(JS_CONTENT)
        
    # 3. Process all HTML files
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Replace old lang switcher with new one
        if OLD_HTML_REGEX.search(content):
            content = OLD_HTML_REGEX.sub(HTML_CONTENT, content)
            modified = True
            
        # Remove old injected style
        if OLD_STYLE_REGEX.search(content):
            content = OLD_STYLE_REGEX.sub('', content)
            modified = True
            
        # Inject lang-switcher.js if not present
        if 'lang-switcher.js' not in content:
            content = content.replace('</body>', '    <script src="lang-switcher.js"></script>\\n</body>')
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")

if __name__ == '__main__':
    main()
