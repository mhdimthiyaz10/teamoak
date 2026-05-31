import os
import re

files_to_convert = [
    "tobacco-trading.html",
    "food-stuff-trading.html",
    "kizhisseri-jewellers.html",
    "general-trading.html",
    "best-vibes-contracting.html",
    "team-oak-hotels.html",
    "team-oak-camps.html",
    "mamichi-apartments.html",
    "oak-architects.html",
    "bubbl.html",
    "team-oak-transport.html",
    "team-oak-safety.html",
    "cafein.html",
    "pharma-fleet.html"
]

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"

for filename in files_to_convert:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the img tag inside .nav-logo
    # <a href="index.html" class="nav-logo">
    #     <img src="assets/logo.png.png" alt="Team Oak Logo">
    # </a>
    
    # Let's just add the style directly to the img tag
    content = content.replace('<img src="assets/logo.png.png" alt="Team Oak Logo">', '<img src="assets/logo.png.png" alt="Team Oak Logo" style="filter: brightness(0) invert(1) !important;">')
    
    # Also fix the CSS block to add !important if it doesn't have it
    content = content.replace('filter: brightness(0) invert(1); }', 'filter: brightness(0) invert(1) !important; }')
    
    # Also, some other files might use a different logo path? Unlikely if they are all identical.
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully applied inline white logo filter to {filename}")
