import os
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"

# 1. Update about.html
about_path = os.path.join(base_dir, "about.html")
if os.path.exists(about_path):
    with open(about_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Swap CSS variables
    content = re.sub(r'--black:\s*#[a-f0-9]+;', '--black: #ffffff;', content)
    content = re.sub(r'--white:\s*#[a-f0-9]+;', '--white: #0a0a0a;', content)
    content = re.sub(r'--off-white:\s*#[a-f0-9]+;', '--off-white: #121212;', content)
    content = re.sub(r'--light:\s*#[a-f0-9]+;', '--light: #2a2a2a;', content)
    content = re.sub(r'--dark:\s*#[a-f0-9]+;', '--dark: #eeeeee;', content)
    
    # Nav background
    content = content.replace('background: rgba(255,255,255,0.94);', 'background: rgba(10,10,10,0.85);')
    content = content.replace('border-bottom: 1px solid rgba(0,0,0,0.07);', 'border-bottom: 1px solid rgba(255,255,255,0.05);')
    
    # Dropdown
    content = content.replace('background: rgba(255,255,255,0.98);', 'background: rgba(20,20,20,0.98);')
    content = content.replace('color: #1a1a1a;', 'color: #eeeeee;')
    content = content.replace('background: rgba(0,0,0,0.03);', 'background: rgba(255,255,255,0.05);')
    content = content.replace('color: #444;', 'color: #aaaaaa;')
    content = content.replace('color: #333;', 'color: #bbbbbb;')
    content = content.replace('border: 1px solid rgba(0,0,0,0.04);', 'border: 1px solid rgba(255,255,255,0.05);')

    # Hero gradient
    content = content.replace('rgba(255,255,255,0.72)', 'rgba(10,10,10,0.85)')
    content = content.replace('rgba(255,255,255,0.28)', 'rgba(10,10,10,0.5)')
    content = content.replace('rgba(255,255,255,0.10)', 'rgba(10,10,10,0.2)')
    content = content.replace('rgba(255,255,255,0.9)', 'rgba(10,10,10,0.95)')

    # Values desc background
    content = content.replace('background: #f8f8f8;', 'background: #151515;')
    content = content.replace('background: #f0f0f0;', 'background: #1f1f1f;')
    content = content.replace('color: #444;', 'color: #cccccc;')
    content = content.replace('color: #555;', 'color: #bbbbbb;')
    content = content.replace('color: #666;', 'color: #999999;')

    # Global presence card
    content = content.replace('background: rgba(201,168,76,0.06);', 'background: rgba(201,168,76,0.1);')
    
    # White logo for nav
    content = content.replace('<img src="assets/logo.png.png" alt="Team Oak Logo">', '<img src="assets/logo.png.png" alt="Team Oak Logo" style="filter: brightness(0) invert(1) !important;">')
    
    # Footer
    def replace_minimal_footer(match):
        block = match.group(0)
        block = block.replace('background-color: var(--bg-dark, #0a0a0a);', 'background-color: #0d0d0d;')
        block = block.replace('background-color: #ffffff;', 'background-color: #0d0d0d;')
        block = block.replace('color: #111111;', 'color: #ffffff;')
        block = block.replace('color: #555555;', 'color: #999999;')
        block = block.replace('color: #888888;', 'color: #777777;')
        block = block.replace('border-top: 1px solid rgba(0,0,0,0.08);', 'border-top: 1px solid rgba(255,255,255,0.05);')
        return block
        
    content = re.sub(r'/\*\s*MINIMAL STANDARD FOOTER.*?@media.*?\}', replace_minimal_footer, content, flags=re.DOTALL)
    
    # Mega Menu
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

    # Js nav background
    content = content.replace("nav.style.background = 'rgba(255,255,255,0.98)';", "nav.style.background = 'rgba(10,10,10,0.95)';")
    content = content.replace("nav.style.background = 'rgba(255,255,255,0.94)';", "nav.style.background = 'rgba(10,10,10,0.85)';")

    with open(about_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated about.html")


# 2. Update media.html, career.html, contact.html
for filename in ["media.html", "career.html", "contact.html"]:
    filepath = os.path.join(base_dir, filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change variable colors
    content = re.sub(r'--bg-dark:\s*#ffffff;', '--bg-dark: #0d0d0d;', content)
    content = re.sub(r'--bg-charcoal:\s*#f9f9fb;', '--bg-charcoal: #151515;', content)
    content = re.sub(r'--bg-card:\s*#f3f4f6;', '--bg-card: #1f1f1f;', content)
    content = re.sub(r'--text-light:\s*#111111;', '--text-light: #ffffff;', content)
    content = re.sub(r'--text-muted:\s*#555555;', '--text-muted: #999999;', content)
    content = re.sub(r'--border-color:\s*rgba\(0,\s*0,\s*0,\s*0\.08\);', '--border-color: rgba(255, 255, 255, 0.08);', content)

    # 2. Page Hero gradient
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
    
    # White logo for nav
    content = content.replace('<img src="assets/logo.png.png" alt="Team Oak Logo">', '<img src="assets/logo.png.png" alt="Team Oak Logo" style="filter: brightness(0) invert(1) !important;">')

    # Media cards (if any)
    content = content.replace('background: rgba(255, 255, 255, 0.7);', 'background: rgba(25, 25, 25, 0.7);')
    content = content.replace('border: 1px solid rgba(255, 255, 255, 0.8);', 'border: 1px solid rgba(255, 255, 255, 0.1);')
    content = content.replace('color: #111;', 'color: #fff;')
    content = content.replace('color: #333;', 'color: #ddd;')
    content = content.replace('background: #f0f0f0;', 'background: #111;')

    # Event cards
    content = content.replace('background-color: #efede7;', 'background-color: var(--bg-charcoal);')
    content = content.replace('color: #222;', 'color: #eee;')
    content = content.replace('background: #ffffff;', 'background: #111111;')
    content = content.replace('color: #444;', 'color: #ccc;')

    # Form (Contact)
    content = content.replace('background: #f8f8f8;', 'background: #1c1c1c;')
    content = content.replace('border: 1px solid #e0e0e0;', 'border: 1px solid #333;')
    content = content.replace('color: #333;', 'color: #eee;')
    content = content.replace('background: rgba(0,0,0,0.03);', 'background: rgba(255,255,255,0.05);')
    content = content.replace('border-bottom: 2px solid #000;', 'border-bottom: 2px solid #fff;')
    
    # Jobs (Career)
    content = content.replace('border: 1px solid #eee;', 'border: 1px solid #222;')
    content = content.replace('background: rgba(0,0,0,0.02);', 'background: rgba(255,255,255,0.02);')
    
    # 8. MINIMAL STANDARD FOOTER
    content = re.sub(r'/\*\s*MINIMAL STANDARD FOOTER.*?@media.*?\}', replace_minimal_footer, content, flags=re.DOTALL)
    
    # 9. MEGA MENU OVERRIDE
    content = re.sub(r'/\*\s*MEGA MENU OVERRIDE.*?</style>', replace_mega_menu, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
