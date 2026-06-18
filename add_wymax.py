import os
import glob

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

nav_target = '<li><a href="pharma-fleet.html">Pharma Fleet</a></li>'
nav_addition = '\n                            <li><a href="wymax-media.html">WYMAX MEDIA</a></li>'

footer_target = '<li><a href="bubbl.html">Bubbl</a></li>'
footer_addition = '\n                        <li><a href="wymax-media.html">WYMAX MEDIA</a></li>'

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # 1. Main navigation
    if nav_target in content and 'WYMAX MEDIA' not in content:
        content = content.replace(nav_target, nav_target + nav_addition)
        modified = True

    # 2. Footer navigation
    # Be careful not to replace it multiple times if bubbl.html is mentioned elsewhere.
    # The footer bubbl has this indentation: "                        <li><a href=\"bubbl.html\">Bubbl</a></li>"
    # Actually, let's use a more specific target for footer if possible, or just replace it.
    footer_target_specific = '                        <li><a href="bubbl.html">Bubbl</a></li>\n                    </ul>\n                </div>'
    footer_addition_specific = '                        <li><a href="bubbl.html">Bubbl</a></li>\n                        <li><a href="wymax-media.html">WYMAX MEDIA</a></li>\n                    </ul>\n                </div>'
    
    if footer_target_specific in content and 'wymax-media.html' not in content:
        content = content.replace(footer_target_specific, footer_addition_specific)
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
