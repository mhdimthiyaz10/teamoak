import os
import re
import glob

def remove_lang_switcher():
    html_files = glob.glob('*.html')
    
    # Regex to match the mobile switcher block
    mobile_pattern = re.compile(
        r'<li class="mobile-switcher-li">.*?<div class="premium-lang-switcher mobile-switcher">.*?</div>.*?</li>',
        re.DOTALL
    )
    
    # Regex to match the desktop switcher block
    desktop_pattern = re.compile(
        r'<div class="premium-lang-switcher desktop-switcher">.*?</div>\s*</div>',
        re.DOTALL
    )

    # Some files might have different spacing, let's use a simpler approach based on start/end tags if possible, or just re.DOTALL.
    # The desktop switcher is usually inside:
    # <div class="nav-actions" ...>
    # <a href="contact.html" class="hero-nav-cta">Contact Us</a>
    # <div class="premium-lang-switcher desktop-switcher">...</div>
    # </div>
    # So if we just remove the premium-lang-switcher desktop-switcher div...

    desktop_pattern_clean = re.compile(
        r'<div class="premium-lang-switcher desktop-switcher">.*?</div>\n\s*</div>',
        re.DOTALL
    )
    
    desktop_pattern_generic = re.compile(
        r'<div class="premium-lang-switcher desktop-switcher">[\s\S]*?(?=</div>\n</div>)</div>',
        re.DOTALL
    )

    desktop_pattern_exact = re.compile(
        r'<div class="premium-lang-switcher desktop-switcher">.*?</div>\n(?:</div>)?',
        re.DOTALL
    )

    # Since HTML parsing with regex is hard, let's use a more robust search and replace based on the known string blocks, 
    # or a balanced parser if necessary. But regex with non-greedy might work if we are careful about the closing div.
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        
        # Remove mobile switcher
        content = re.sub(r'<li class="mobile-switcher-li">\s*<div class="premium-lang-switcher mobile-switcher">[\s\S]*?</div>\s*</div>\s*</li>', '', content)
        content = re.sub(r'<li class="mobile-switcher-li">[\s\S]*?</li>', '', content)
        
        # Remove desktop switcher
        # We need to be careful not to remove the closing </div> of the parent if it's not part of the switcher.
        # The desktop switcher has two nested divs (pls-dropdown)
        # `<div class="premium-lang-switcher desktop-switcher"> ... <div class="pls-dropdown"> ... </div> ... </div>`
        content = re.sub(r'<div class="premium-lang-switcher desktop-switcher">\s*<button class="pls-btn"[\s\S]*?<div class="pls-dropdown">[\s\S]*?</div>\s*</div>', '', content)

        # Remove the script tag
        content = re.sub(r'<script src="lang-switcher\.js"></script>\s*', '', content)

        if content != original_content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")
        else:
            print(f"No changes in {file}")

if __name__ == '__main__':
    remove_lang_switcher()
