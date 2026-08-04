import os
import glob
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

js_hover_pattern = re.compile(
    r"\s*// Still allow hover for a premium feel, but click \"locks\" it\s*"
    r"li\.addEventListener\('mouseenter', function\(\) \{\s*"
    r"if \(!li\.classList\.contains\('open'\)\) \{\s*"
    r"var siblings = li\.parentElement\.querySelectorAll\(':scope > \.open'\);\s*"
    r"siblings\.forEach\(function\(s\) \{ s\.classList\.remove\('open'\); \}\);\s*"
    r"li\.classList\.add\('open'\);\s*"
    r"\}\s*"
    r"\}\);", re.MULTILINE | re.DOTALL)

js_hover_pattern_2 = re.compile(
    r"\s*li\.addEventListener\('mouseenter', \(\) => li\.classList\.add\('open'\)\);", re.MULTILINE | re.DOTALL)

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Remove arrow pointing to dropdown
    arrow_override = ".nav-links li.has-arrow .dropdown::before { display: none !important; }"
    if "MEGA MENU OVERRIDE V5" in content and arrow_override not in content:
        content = content.replace("/* ═══════════════════════════\n           MEGA MENU OVERRIDE V5", 
                                  "/* ═══════════════════════════\n           MEGA MENU OVERRIDE V5\n        ═══════════════════════════ */\n        " + arrow_override + "\n        /*")
        modified = True
    elif ".nav-links li.has-arrow .dropdown::before {" in content:
        # Some files might not have MEGA MENU OVERRIDE V5, but have the before pseudo element
        if arrow_override not in content:
            content = content.replace("</head>", f"    <style>{arrow_override}</style>\n</head>")
            modified = True

    # 2. Remove mouseenter JS
    if js_hover_pattern.search(content):
        content = js_hover_pattern.sub("", content)
        modified = True
        
    if js_hover_pattern_2.search(content):
        content = js_hover_pattern_2.sub("", content)
        modified = True

    # Ensure there is no CSS hover triggering the main dropdown
    css_hover_pattern = re.compile(r"\.nav-links li\.has-arrow:hover \.dropdown\s*{[^}]*}", re.MULTILINE)
    if css_hover_pattern.search(content):
        content = css_hover_pattern.sub("/* hover removed */", content)
        modified = True
        
    css_hover_pattern_hero = re.compile(r"\.hero-nav-links li\.has-arrow:hover \.dropdown\s*{[^}]*}", re.MULTILINE)
    if css_hover_pattern_hero.search(content):
        content = css_hover_pattern_hero.sub("/* hover removed */", content)
        modified = True
        
    # And for multiple selectors separated by comma
    multi_hover_pattern = re.compile(r"\.nav-links li\.has-arrow:hover \.dropdown\s*,")
    if multi_hover_pattern.search(content):
        content = multi_hover_pattern.sub("", content)
        modified = True
        
    multi_hover_pattern_hero = re.compile(r"\.hero-nav-links li\.has-arrow:hover \.dropdown\s*,")
    if multi_hover_pattern_hero.search(content):
        content = multi_hover_pattern_hero.sub("", content)
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
