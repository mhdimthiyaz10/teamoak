import os
import re
import json

def fix_json_files():
    # Update en.json
    with open('en.json', 'r', encoding='utf-8') as f:
        en_data = json.load(f)
    
    if "global_home_2" in en_data:
        en_data["global_home_2"] = "Home"
    if "global_about_us_2" in en_data:
        en_data["global_about_us_2"] = "About Us"
        
    with open('en.json', 'w', encoding='utf-8') as f:
        json.dump(en_data, f, ensure_ascii=False, indent=4)

    # Update ar.json
    with open('ar.json', 'r', encoding='utf-8') as f:
        ar_data = json.load(f)
        
    if "global_home_2" in ar_data:
        ar_data["global_home_2"] = "الصفحة الرئيسية"
    if "global_about_us_2" in ar_data:
        ar_data["global_about_us_2"] = "معلومات عنا"
        
    with open('ar.json', 'w', encoding='utf-8') as f:
        json.dump(ar_data, f, ensure_ascii=False, indent=4)

def fix_html_files():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    keys_to_fix = [
        "global_home_2",
        "global_about_us_2"
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
            
            return f'<li{li_before}{li_after}><a data-i18n="{key}"{a_attrs}>{inner_text}</a></li>'
            
        new_content, count = pattern.subn(replacer, content)
        
        if count > 0:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {count} instances in {file}")
            total_fixed += count
            
    print(f"Total instances fixed in HTML: {total_fixed}")

if __name__ == '__main__':
    fix_json_files()
    fix_html_files()
