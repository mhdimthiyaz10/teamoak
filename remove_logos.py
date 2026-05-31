import os
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
files_to_update = [
    "best-vibes-contracting.html",
    "kizhisseri-jewellers.html",
    "mamichi-apartments.html"
]

for filename in files_to_update:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change grid-template-columns from 2fr 1fr to 1fr
    content = content.replace('grid-template-columns: 2fr 1fr;', 'grid-template-columns: 1fr;')
    
    # Remove the entire logo-placeholder-container block
    # We can use a regex that looks for <div class="logo-placeholder-container ...</div>
    # It spans multiple lines, so we use DOTALL
    pattern = r'\s*<div class="logo-placeholder-container[^>]*>.*?</div>\s*</div>'
    
    # Wait, the inner div might cause issues if there are multiple nested divs.
    # The structure is:
    # <div class="logo-placeholder-container fu d2">
    #     <div class="logo-image-wrapper">
    #         <img src="..." ...>
    #     </div>
    # </div>
    # Let's match it accurately:
    pattern = r'\s*<div class="logo-placeholder-container[^>]*>\s*<div class="logo-image-wrapper">\s*<img[^>]*>\s*</div>\s*</div>'
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filename}")
