import os
from bs4 import BeautifulSoup

def fix_switcher():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        modified = False
        # Find all switchers
        switchers = soup.find_all(class_='premium-lang-switcher')
        for switcher in switchers:
            # Remove data-i18n from switcher itself
            if switcher.has_attr('data-i18n'):
                del switcher['data-i18n']
                modified = True
                
            # Remove data-i18n from all descendants
            for desc in switcher.find_all():
                for attr in ['data-i18n', 'data-i18n-placeholder', 'data-i18n-alt']:
                    if desc.has_attr(attr):
                        del desc[attr]
                        modified = True
                        
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Fixed switcher annotations in {file}")

if __name__ == '__main__':
    fix_switcher()
