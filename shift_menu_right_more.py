import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # We want to increase the margin-left from 30px to 60px in the MENU SHIFT RIGHT FIX block
    if '<!-- MENU SHIFT RIGHT FIX -->' in content:
        # For the dropdown
        content = content.replace('margin-left: 30px !important;', 'margin-left: 60px !important;')
        content = content.replace('width: calc(100% - 30px) !important;', 'width: calc(100% - 60px) !important;')
        
        # For the nested flyout
        content = content.replace('margin-left: 20px !important;', 'margin-left: 40px !important;')
        content = content.replace('width: calc(100% - 20px) !important;', 'width: calc(100% - 40px) !important;')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
