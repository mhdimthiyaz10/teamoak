import os
import glob

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the hover trigger for dropdown
    new_content = content.replace('.nav-links li.has-arrow:hover .dropdown { opacity: 1; pointer-events: all; transform: translateX(-50%) translateY(0); }', '/* .nav-links li.has-arrow:hover .dropdown { ... } removed to enforce click only */')
    new_content = new_content.replace('.nav-links li.has-arrow:hover > a::after { transform: rotate(225deg) translateY(2px); }', '.nav-links li.has-arrow.open > a::after { transform: rotate(225deg) translateY(2px); }')

    # Also check if there's any other hover rules for dropdown in the style block
    new_content = new_content.replace('.nav-links li.has-arrow:hover .dropdown { opacity: 1; pointer-events: all; }', '')
    
    # And there might be a rule without the transform:
    # just look for typical hover dropdowns
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
