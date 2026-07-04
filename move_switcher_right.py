import glob
import re

def main():
    html_files = glob.glob('*.html')
    # Match the switcher followed by the CTA button
    pattern = re.compile(r'(<div class="premium-lang-switcher">.*?</div>)\s*(<a[^>]*class="[^"]*(?:hero-nav-cta|nav-btn)[^"]*"[^>]*>.*?</a>)', re.DOTALL)
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = pattern.sub(r'\2\n\n\1', content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Swapped switcher to the right of CTA in {file}")
            
    # Also update style.css to fix margins since it is now the rightmost element
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write('\n/* Push Switcher to the Right Edge */\n')
        f.write('.premium-lang-switcher { margin-right: 0 !important; margin-left: 20px !important; }\n')
        f.write('html[dir="rtl"] .premium-lang-switcher { margin-right: 20px !important; margin-left: 0 !important; }\n')

if __name__ == '__main__':
    main()
