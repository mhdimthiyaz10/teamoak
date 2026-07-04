import glob
import re

def fix_html_files():
    html_files = glob.glob('*.html')
    
    # We want to match:
    # <a ... class="nav-btn" ...>...</a> OR <a ... class="hero-nav-cta" ...>...</a>
    # Followed by:
    # <div class="premium-lang-switcher desktop-switcher"> ... </div>
    
    # Wait, they are currently in the order:
    # <a ...>
    # <div class="premium-lang-switcher desktop-switcher">...</div>
    
    # We want to wrap them in:
    # <div class="nav-actions" style="display: flex; align-items: center; justify-content: flex-end; gap: 1rem;">
    #   <a ...>
    #   <div ...>
    # </div>
    
    # Let's use a regex to find both and replace them with the wrapped version.
    # The regex needs to be careful not to double wrap if we run it multiple times.
    
    pattern = re.compile(
        r'(<a[^>]*class="[^"]*(?:hero-nav-cta|nav-btn)[^"]*"[^>]*>.*?</a>)\s*'
        r'(<div class="premium-lang-switcher desktop-switcher">.*?</div>\s*</div>)', # The switcher has an inner div, so it ends with </div></div>
        re.DOTALL
    )
    
    # Let's make a more robust pattern that parses until the end of the switcher.
    # The switcher is known to have <div class="pls-dropdown">...</div> inside it.
    
    pattern2 = re.compile(
        r'(<a[^>]*class="[^"]*(?:hero-nav-cta|nav-btn)[^"]*"[^>]*>.*?</a>)\s*'
        r'(<div class="premium-lang-switcher desktop-switcher">.*?</button>\s*<div class="pls-dropdown">.*?</div>\s*</div>)',
        re.DOTALL
    )
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Avoid double wrapping
        if '<div class="nav-actions"' in content:
            continue
            
        new_content = pattern2.sub(r'<div class="nav-actions" style="display: flex; align-items: center; justify-content: flex-end; gap: 0.5rem;">\n\1\n\2\n</div>', content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {file}")

if __name__ == '__main__':
    fix_html_files()
