import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # We want to increase the margin-left from 60px to 100px in the MENU SHIFT RIGHT FIX block
    if '<!-- MENU SHIFT RIGHT FIX -->' in content:
        # For the main dropdown
        content = content.replace('margin-left: 60px !important;', 'margin-left: 100px !important;')
        content = content.replace('width: calc(100% - 60px) !important;', 'width: calc(100% - 100px) !important;')
        
        # For the nested flyout
        content = content.replace('margin-left: 40px !important;', 'margin-left: 60px !important;')
        content = content.replace('width: calc(100% - 40px) !important;', 'width: calc(100% - 60px) !important;')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
