import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

target_str = 'href="#">YouTube</a>'
replacement_str = 'href="https://youtube.com/@theoakteam8268?si=32MAruPZFb6WyC8a" target="_blank">YouTube</a>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    content = content.replace(target_str, replacement_str)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
