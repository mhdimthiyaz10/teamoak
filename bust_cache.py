import os
import re

def bust_cache():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace i18n.css with i18n.css?v=6
        new_content = re.sub(r'href=["\']i18n\.css(\?v=\d+)?["\']', 'href="i18n.css?v=6"', content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Busted cache for i18n.css in {file}")

if __name__ == '__main__':
    bust_cache()
