import os
import glob
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. Remove the hover rule for the main dropdown
    # It can be `.nav-links li.has-arrow:hover .dropdown, \n .nav-links li.has-arrow.open .dropdown`
    # or `.nav-links li.has-arrow:hover .dropdown, .nav-links li.has-arrow.open .dropdown`
    content = re.sub(r'\.nav-links\s+li\.has-arrow:hover\s+\.dropdown\s*,', '', content)
    
    # 2. Remove the hover rule for the dropdown arrow rotation
    content = re.sub(r'\.nav-links\s+li\.has-arrow:hover\s*>\s*a::after\s*,', '', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
