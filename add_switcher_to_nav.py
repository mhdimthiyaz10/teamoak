import glob
import re

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

def main():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Don't add if already there
        if 'premium-lang-switcher' not in content:
            new_content = re.sub(r'(<a[^>]*class="[^"]*(?:hero-nav-cta|nav-btn)[^"]*"[^>]*>.*?</a>)', 
                                 HTML_CONTENT + r'\n\1', content)
            
            if new_content != content:
                content = new_content
                modified = True
        
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added switcher to {file}")

if __name__ == '__main__':
    main()
