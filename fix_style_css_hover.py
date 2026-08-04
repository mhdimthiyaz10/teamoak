import os
import re

filepath = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm\style.css"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

modified = False

css_hover_pattern_hero = re.compile(r"\.hero-nav-links li\.has-arrow:hover \.dropdown\s*{[^}]*}", re.MULTILINE)
if css_hover_pattern_hero.search(content):
    content = css_hover_pattern_hero.sub("/* hover removed */", content)
    modified = True
    
multi_hover_pattern_hero = re.compile(r"\.hero-nav-links li\.has-arrow:hover \.dropdown\s*,")
if multi_hover_pattern_hero.search(content):
    content = multi_hover_pattern_hero.sub("", content)
    modified = True

if modified:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {os.path.basename(filepath)}")
else:
    print(f"No changes needed in {os.path.basename(filepath)}")
