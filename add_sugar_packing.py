import os
import re
import json

def fix_json_files():
    # Update en.json
    with open('en.json', 'r', encoding='utf-8') as f:
        en_data = json.load(f)
    
    if "about_sugar_packing_unit" in en_data:
        en_data["about_sugar_packing_unit"] = "Sugar packing Unit"
        
    with open('en.json', 'w', encoding='utf-8') as f:
        json.dump(en_data, f, ensure_ascii=False, indent=4)

    # Update ar.json
    with open('ar.json', 'r', encoding='utf-8') as f:
        ar_data = json.load(f)
        
    if "about_sugar_packing_unit" in ar_data:
        # Extract just the text from the HTML tag if present
        text = ar_data["about_sugar_packing_unit"]
        match = re.search(r'>([^<]+)<', text)
        if match:
            ar_data["about_sugar_packing_unit"] = match.group(1)
        elif '<a' not in text:
             pass # Already pure text
             
    with open('ar.json', 'w', encoding='utf-8') as f:
        json.dump(ar_data, f, ensure_ascii=False, indent=4)

def update_footer():
    files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # We will search for the last item in the footer ventures list
    # and append the new item right after it.
    
    search_str = '<li data-i18n="about_makeen_spareparts_trading"><a href="makin-spare-parts-trading.html">Makeen SpareParts Trading</a></li>'
    insert_str = '<li data-i18n="about_makeen_spareparts_trading"><a href="makin-spare-parts-trading.html">Makeen SpareParts Trading</a></li>\n<li data-i18n="about_sugar_packing_unit"><a href="sugar-packing.html">Sugar packing Unit</a></li>'
    
    total_updated = 0
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if search_str in content and 'sugar-packing.html' not in content[content.find(search_str):content.find(search_str)+200]:
            new_content = content.replace(search_str, insert_str)
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added to {file}")
            total_updated += 1
            
    print(f"Total files updated: {total_updated}")

if __name__ == '__main__':
    fix_json_files()
    update_footer()
