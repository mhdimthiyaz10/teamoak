import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

target_str = 'href="#">Instagram</a>'
replacement_str = 'href="https://www.instagram.com/_oak_architects?igsh=a3lnM3pucXB3djk2" target="_blank">Instagram</a>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    content = content.replace(target_str, replacement_str)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
