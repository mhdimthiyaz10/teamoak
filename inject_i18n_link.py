import os
from bs4 import BeautifulSoup

def inject_link():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        if soup.head:
            # Check if i18n.css is already linked
            if not soup.find('link', href='i18n.css'):
                link_tag = soup.new_tag('link', rel='stylesheet', href='i18n.css')
                soup.head.append(link_tag)
                
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(str(soup))
                print(f"Injected i18n.css link into {file}")

if __name__ == '__main__':
    inject_link()
