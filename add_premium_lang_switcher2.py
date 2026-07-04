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

OLD_HTML_REGEX = re.compile(r'<div class="lang-switcher">.*?</div>', re.DOTALL)
OLD_STYLE_REGEX = re.compile(r'<style>\s*/\*\s*Language Switcher\s*\*/.*?</style>', re.DOTALL)

def main():
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
            content = content.replace('</body>', '    <script src="lang-switcher.js"></script>\n</body>')
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")

if __name__ == '__main__':
    main()
