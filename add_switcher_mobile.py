import glob
import re

CSS_APPEND = """
/* Dual Switcher Handling for Desktop/Mobile */
.desktop-switcher {
    display: inline-flex;
}
.mobile-switcher-li {
    display: none;
    list-style: none;
    margin-top: 15px;
    padding-left: 0;
}
@media (max-width: 768px) {
    .desktop-switcher { display: none !important; }
    .mobile-switcher-li { display: block !important; margin-bottom: 2rem; }
    .premium-lang-switcher.mobile-switcher { margin-left: 0 !important; margin-right: 0 !important; }
    html[dir="rtl"] .premium-lang-switcher.mobile-switcher { margin-left: 0 !important; margin-right: 0 !important; }
}
"""

HTML_MOBILE_SWITCHER = """<li class="mobile-switcher-li">
    <div class="premium-lang-switcher mobile-switcher">
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
</li>"""

def main():
    # Append CSS
    with open('style.css', 'r', encoding='utf-8') as f:
        style_content = f.read()
    if '.mobile-switcher-li' not in style_content:
        with open('style.css', 'a', encoding='utf-8') as f:
            f.write(CSS_APPEND)

    # Process HTML files
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # 1. Change existing switcher to desktop-switcher
        if '<div class="premium-lang-switcher">' in content:
            content = content.replace('<div class="premium-lang-switcher">', '<div class="premium-lang-switcher desktop-switcher">')
            modified = True
            
        # 2. Insert mobile switcher after mobile-contact li
        pattern = re.compile(r'(<li class="mobile-contact">.*?</li>)', re.DOTALL)
        if '<li class="mobile-switcher-li">' not in content:
            new_content = pattern.sub(r'\1\n' + HTML_MOBILE_SWITCHER, content)
            if new_content != content:
                content = new_content
                modified = True
                
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")

if __name__ == '__main__':
    main()
