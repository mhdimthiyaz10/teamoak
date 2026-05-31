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

def update_footer(content):
    # Update background colors
    content = content.replace('background-color: #ffffff;', 'background-color: #0d0d0d;')
    # For .minimal-footer { background-color: ... } specifically if it differs
    content = re.sub(r'\.minimal-footer\s*\{[^}]*?background-color:\s*#[a-fA-F0-9]+;', r'.minimal-footer {\n            background-color: #0d0d0d;', content)
    
    # Update general color properties in minimal-footer blocks
    # We will look for `.minimal-footer { ... }` up to the next media query or </style>
    
    # Actually, simpler: just do global replacements that apply to the footer CSS
    # Since these files mostly contain only this custom CSS in <style> blocks
    
    # The minimal-footer text color
    content = content.replace('color: #111111;', 'color: #ffffff;')
    
    # The hover color
    content = content.replace('.mf-col ul li a:hover { color: #111111; }', '.mf-col ul li a:hover { color: #ffffff; }')
    content = content.replace('.mf-legal a:hover { color: #111111; }', '.mf-legal a:hover { color: #ffffff; }')
    
    # The border
    content = content.replace('border-top: 1px solid rgba(0,0,0,0.08);', 'border-top: 1px solid rgba(255,255,255,0.05);')
    content = content.replace('box-shadow: 0 0 0 1px rgba(0,0,0,0.08);', 'box-shadow: 0 0 0 1px rgba(255,255,255,0.08);')
    
    # Any other specific matches from the footer
    content = content.replace('.mf-col h4 { font-family: \'Outfit\', sans-serif; font-size: 1.15rem; font-weight: 700; color: #111111;', '.mf-col h4 { font-family: \'Outfit\', sans-serif; font-size: 1.15rem; font-weight: 700; color: #ffffff;')

    # Fix dropdown colors which might have been accidentally replaced by color: #ffffff; instead of #111111;
    # But wait, these dropdowns might also use #111111. Let's make sure we only replace in the footer block.
    return content

for filename in files_to_convert:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filename}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the block starting with .minimal-footer and ending at </style>
    # or just use a function
    
    match = re.search(r'(\.minimal-footer\s*\{.*?</style>)', content, flags=re.DOTALL)
    if match:
        original_block = match.group(1)
        new_block = original_block.replace('background-color: #ffffff;', 'background-color: #0d0d0d;')
        new_block = new_block.replace('color: #111111;', 'color: #ffffff;')
        new_block = new_block.replace('border-top: 1px solid rgba(0,0,0,0.08);', 'border-top: 1px solid rgba(255,255,255,0.05);')
        new_block = new_block.replace('box-shadow: 0 0 0 1px rgba(0,0,0,0.08);', 'box-shadow: 0 0 0 1px rgba(255,255,255,0.08);')
        
        # Avoid touching the mega menu override which is also in <style>
        # Let's just be more precise with the footer block.
        # Find the text between .minimal-footer { and @media
        pass

    # Actually, a better way is to split the content by "MINIMAL STANDARD FOOTER" and "MEGA MENU OVERRIDE"
    parts = re.split(r'(/\*\s*═══════════════════════════\s*MINIMAL STANDARD FOOTER.*?\*/)', content, flags=re.DOTALL)
    
    if len(parts) >= 3:
        # We have the footer comment. The footer CSS is in the part after the comment.
        # We also want to stop at the next comment or end of style.
        # Let's just apply the replacement to the part that comes after the footer comment until the mega menu comment
        
        footer_css_part = parts[2]
        
        footer_css_part = footer_css_part.replace('background-color: #ffffff;', 'background-color: #0d0d0d;')
        footer_css_part = footer_css_part.replace('color: #111111;', 'color: #ffffff;')
        footer_css_part = footer_css_part.replace('color: #555555;', 'color: #999999;')
        footer_css_part = footer_css_part.replace('color: #888888;', 'color: #777777;')
        footer_css_part = footer_css_part.replace('border-top: 1px solid rgba(0,0,0,0.08);', 'border-top: 1px solid rgba(255,255,255,0.05);')
        footer_css_part = footer_css_part.replace('box-shadow: 0 0 0 1px rgba(0,0,0,0.08);', 'box-shadow: 0 0 0 1px rgba(255,255,255,0.08);')
        
        new_content = parts[0] + parts[1] + footer_css_part
        
        for i in range(3, len(parts)):
            new_content += parts[i]
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {filename}")
    else:
        # If the comment is missing, we just replace .minimal-footer block
        new_content = content
        
        def replace_bg(m):
            return m.group(0).replace(m.group(1), '#0d0d0d')
            
        new_content = re.sub(r'(\.minimal-footer\s*\{[^}]*?background-color:\s*)(#[a-fA-F0-9]+);', replace_bg, new_content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Successfully updated {filename} (Regex fallback)")
        else:
            print(f"No changes made to {filename}")
