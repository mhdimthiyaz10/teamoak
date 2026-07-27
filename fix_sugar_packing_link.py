import os
import re

def fix_sugar_packing_links():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Matches <li ... data-i18n="about_sugar_packing_unit" ...><a ...>...</a></li>
    pattern = re.compile(
        r'<li([^>]*)data-i18n="about_sugar_packing_unit"([^>]*)>\s*<a([^>]*)>(.*?)</a>\s*</li>',
        re.IGNORECASE | re.DOTALL
    )
    
    total_fixed = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def replacer(m):
            li_before = m.group(1)
            li_after = m.group(2)
            a_attrs = m.group(3)
            inner_text = m.group(4)
            
            return f'<li{li_before}{li_after}><a data-i18n="about_sugar_packing_unit"{a_attrs}>{inner_text}</a></li>'
            
        new_content, count = pattern.subn(replacer, content)
        
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {count} instances in {file}")
            total_fixed += count
            
    print(f"Total instances fixed: {total_fixed}")

if __name__ == '__main__':
    fix_sugar_packing_links()
