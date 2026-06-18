import os
import glob
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

nav_target = '<li><a href="wymax-media.html">WYMAX MEDIA</a></li>'
nav_addition = '\n                            <li><a href="team-oak-builders.html">Team Oak Builders &amp; Developers</a></li>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # 1. Main navigation
    if nav_target in content and 'team-oak-builders.html' not in content:
        content = content.replace(nav_target, nav_target + nav_addition)
        modified = True
    elif '<li><a href="pharma-fleet.html">Pharma Fleet</a></li>' in content and 'team-oak-builders.html' not in content:
        # Fallback if WYMAX MEDIA is missing in some nav for some reason
        content = content.replace('<li><a href="pharma-fleet.html">Pharma Fleet</a></li>', 
                                  '<li><a href="pharma-fleet.html">Pharma Fleet</a></li>' + nav_addition)
        modified = True

    # 2. Footer navigation
    # We want to add it to the "Services" list in the footer.
    # The structure is:
    # <h4>Services</h4>
    # <ul>
    #     <li>...</li>
    #     <li>...</li>
    # </ul>
    if 'team-oak-builders.html' not in content:
        # Let's find the Services block in the footer.
        match = re.search(r'(<h4>Services</h4>\s*<ul>.*?)(</ul>)', content, flags=re.DOTALL)
        if match:
            new_block = match.group(1) + '    <li><a href="team-oak-builders.html">Team Oak Builders &amp; Developers</a></li>\n                    ' + match.group(2)
            content = content.replace(match.group(0), new_block)
            modified = True

    # Fix the missing WYMAX MEDIA in footer for wymax-media.html (and any other files if missing)
    if 'wymax-media.html' not in content and '<h4>Services</h4>' in content:
        match = re.search(r'(<h4>Services</h4>\s*<ul>.*?)(</ul>)', content, flags=re.DOTALL)
        if match:
            new_block = match.group(1) + '    <li><a href="wymax-media.html">WYMAX MEDIA</a></li>\n                    ' + match.group(2)
            content = content.replace(match.group(0), new_block)
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
