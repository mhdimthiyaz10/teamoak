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

    # The original line usually is: .nav-logo img { height: 70px; width: auto; }
    # We want to add filter: brightness(0) invert(1);
    
    if 'filter: brightness(0) invert(1);' not in content:
        new_content = re.sub(
            r'(\.nav-logo\s+img\s*\{[^}]*?)\}',
            r'\1 filter: brightness(0) invert(1); }',
            content
        )
        
        # If it doesn't find .nav-logo img, it might be inline style or something else.
        # But let's check if new_content was modified
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully added white logo filter to {filename}")
        else:
            # Let's try adding it manually to the <style> block if it's not found
            if '</style>' in content:
                new_content = content.replace('</style>', '    .nav-logo img { filter: brightness(0) invert(1); }\n</style>', 1)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Successfully added white logo filter (via tag injection) to {filename}")
            else:
                print(f"Could not update {filename}")
    else:
        print(f"Already applied to {filename}")
