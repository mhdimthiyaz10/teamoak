import os
import re

files_to_convert = [
    "sugar-packing.html",
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

    # 1. Remove White Theme Custom Overrides
    content = re.sub(r'/\*\s*White Theme Custom Overrides\s*\*/.*?\}\n', '', content, flags=re.DOTALL)
    content = re.sub(r'body\s*\{\s*--bg-dark:\s*#ffffff;.*?\}\n', '', content, flags=re.DOTALL)

    # 2. Page Hero gradient (if hardcoded)
    content = content.replace('rgba(255, 255, 255, 0.4)', 'rgba(10, 10, 10, 0.5)')
    content = content.replace('rgba(255, 255, 255, 0.1)', 'rgba(10, 10, 10, 0.2)')
    
    # 3. Nav bar
    content = content.replace('background: rgba(255, 255, 255, 0.85);', 'background: rgba(10,10,10,0.85);')
    content = content.replace('border-bottom: 1px solid rgba(0, 0, 0, 0.08);', 'border-bottom: 1px solid rgba(255,255,255,0.05);')
    
    # 4. Nav links
    content = content.replace('color: #555555; text-decoration: none;', 'color: var(--text-muted); text-decoration: none;')
    content = content.replace('a:hover, .nav-links a.active { color: #111111; }', 'a:hover, .nav-links a.active { color: var(--text-light); }')
    content = content.replace('padding-bottom: 4px; color: #111111;', 'padding-bottom: 4px; color: var(--text-light);')
    
    # 5. Nav Button
    content = content.replace('color: #111111; border: 1.5px solid rgba(0, 0, 0, 0.15);', 'color: var(--text-light); border: 1.5px solid var(--border-color);')
    content = content.replace('nav-btn:hover { background: #111111; color: #ffffff; }', 'nav-btn:hover { background: var(--text-light); color: var(--bg-dark); }')
    
    # 6. Dropdown
    content = content.replace('background: rgba(255, 255, 255, 0.98);', 'background: rgba(20,20,20,0.98);')
    content = content.replace('box-shadow: 0 20px 60px rgba(0,0,0,0.1);', 'box-shadow: 0 20px 60px rgba(0,0,0,0.4);')
    content = content.replace('color: #333333;', 'color: #ddd;')
    content = content.replace('background: rgba(0,0,0,0.03);', 'background: rgba(255,255,255,0.05);')
    
    # 7. JS Scroll
    content = content.replace("nav.style.background = 'rgba(255, 255, 255, 0.95)';", "nav.style.background = 'rgba(10,10,10,0.95)';")
    content = content.replace("nav.style.background = 'rgba(255, 255, 255, 0.85)';", "nav.style.background = 'rgba(10,10,10,0.85)';")
    content = content.replace("nav.style.boxShadow = '0 4px 30px rgba(0,0,0,0.05)';", "nav.style.boxShadow = '0 4px 30px rgba(0,0,0,0.5)';")
    
    # 8. MINIMAL STANDARD FOOTER
    def replace_minimal_footer(match):
        block = match.group(0)
        block = block.replace('background-color: #ffffff;', 'background-color: #0d0d0d;')
        block = block.replace('color: #111111;', 'color: #ffffff;')
        block = block.replace('color: #555555;', 'color: #999999;')
        block = block.replace('color: #888888;', 'color: #777777;')
        block = block.replace('border-top: 1px solid rgba(0,0,0,0.08);', 'border-top: 1px solid rgba(255,255,255,0.05);')
        block = block.replace('box-shadow: 0 0 0 1px rgba(0,0,0,0.08);', 'box-shadow: 0 0 0 1px rgba(255,255,255,0.08);')
        return block
        
    content = re.sub(r'/\*\s*MINIMAL STANDARD FOOTER.*?@media.*?\}', replace_minimal_footer, content, flags=re.DOTALL)
    
    # 9. MEGA MENU OVERRIDE
    def replace_mega_menu(match):
        block = match.group(0)
        block = block.replace('background: #ffffff !important;', 'background: #151515 !important;')
        block = block.replace('background: #f7f7f7 !important;', 'background: rgba(255,255,255,0.05) !important;')
        block = block.replace('color: #111111 !important;', 'color: #f0f0f0 !important;')
        block = block.replace('color: #444444 !important;', 'color: #cccccc !important;')
        block = block.replace('box-shadow: 0 10px 40px rgba(0,0,0,0.08) !important;', 'box-shadow: 0 10px 40px rgba(0,0,0,0.4) !important;')
        block = block.replace('background: #e0e0e0 !important;', 'background: #444444 !important;')
        return block

    content = re.sub(r'/\*\s*MEGA MENU OVERRIDE.*?</style>', replace_mega_menu, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Successfully updated {filename}")
