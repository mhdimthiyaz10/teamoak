import os

files_to_update = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files_to_update:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to add overflow: visible !important; to .nav-links li.has-arrow .dropdown
    if "MEGA MENU OVERRIDE" in content and "overflow: visible !important;" not in content:
        # Find the block for .nav-links li.has-arrow .dropdown and add overflow: visible !important;
        # We can just replace "border: none !important;" with "border: none !important;\n            overflow: visible !important;"
        new_content = content.replace("border: none !important;\n        }", "border: none !important;\n            overflow: visible !important;\n        }")
        
        # In case the exact replacement fails due to spacing
        if new_content == content:
            new_content = content.replace("border: none !important;", "border: none !important;\n            overflow: visible !important;")
            
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"Skipping {filename}")
