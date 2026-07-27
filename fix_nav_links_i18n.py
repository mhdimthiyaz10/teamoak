import os
import re

def fix_nav_links():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Keys that we know are pure text in JSON and are mistakenly placed on <li> tags
    keys_to_fix = [
        "global_home",
        "global_media",
        "global_career",
        "global_contact_us",
        "global_media_2",
        "global_career_2"
    ]
    
    keys_regex = "|".join(keys_to_fix)
    
    pattern = re.compile(
        rf'<li([^>]*)data-i18n="({keys_regex})"([^>]*)>\s*<a([^>]*)>(.*?)</a>\s*</li>',
        re.IGNORECASE | re.DOTALL
    )
    
    total_fixed = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        def replacer(m):
            li_before = m.group(1)
            key = m.group(2)
            li_after = m.group(3)
            a_attrs = m.group(4)
            inner_text = m.group(5)
            
            # Map _2 keys back to the pure text key if needed, so it fetches "Media" and not the HTML string
            mapped_key = key.replace('_2', '') if key.endswith('_2') else key
            
            return f'<li{li_before}{li_after}><a data-i18n="{mapped_key}"{a_attrs}>{inner_text}</a></li>'
            
        new_content, count = pattern.subn(replacer, content)
        
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {count} instances in {file}")
            total_fixed += count
            
    print(f"Total instances fixed: {total_fixed}")

if __name__ == '__main__':
    fix_nav_links()
