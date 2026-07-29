import os
import re

def update_files():
    dir_path = '.'
    for filename in os.listdir(dir_path):
        if filename.endswith('.html'):
            filepath = os.path.join(dir_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Find the Trading flyout block
            # It starts with `<li class="has-flyout"><a data-i18n="global_trading"`
            # And ends with its closing `</ul>`
            
            # Using a custom function to process the string
            def replacer(match):
                inner_content = match.group(2)
                # Remove sugar packing unit from this inner content
                inner_content = re.sub(r'<li\s*><a[^>]*href="sugar-packing\.html"[^>]*>Sugar packing Unit</a></li>\s*', '', inner_content)
                return match.group(1) + inner_content + match.group(3)

            # Match from the start of the Trading flyout to its closing ul
            pattern = r'(<li class="has-flyout">\s*<a data-i18n="global_trading"[^>]*>Trading</a>\s*<ul class="flyout">)(.*?)(</ul>)'
            
            new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

if __name__ == '__main__':
    update_files()
