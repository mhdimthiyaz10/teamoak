import os
import glob

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

nav_target = '<li><a href="general-trading.html">Team Oak General Trading Company</a></li>'
nav_addition = '\n                            <li><a href="makin-spare-parts-trading.html">Makin Spare parts Trading Company</a></li>'

footer_target = '<li><a href="general-trading.html">General Trading</a></li>'
footer_addition = '\n                        <li><a href="makin-spare-parts-trading.html">Makin Spare Parts Trading</a></li>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # 1. Main navigation
    if nav_target in content and 'Makin Spare parts Trading Company' not in content:
        content = content.replace(nav_target, nav_target + nav_addition)
        modified = True

    # 2. Footer navigation
    if footer_target in content and 'Makin Spare Parts Trading' not in content:
        content = content.replace(footer_target, footer_target + footer_addition)
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
