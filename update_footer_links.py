import os
import re

replacement = '''                <div class="mf-col">
                    <h4><a href="our-ventures.html" style="color: inherit; text-decoration: none;">Our Ventures</a></h4>
                </div>

                <div class="mf-col">
                    <h4><a href="our-clients.html" style="color: inherit; text-decoration: none;">Our Clients</a></h4>
                </div>'''

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regex to match the Trading & Industry and Services mf-cols
    pattern = r'<div class="mf-col">\s*<h4>Trading &amp; Industry</h4>\s*<ul>.*?</ul>\s*</div>\s*<div class="mf-col">\s*<h4>Services</h4>\s*<ul>.*?</ul>\s*</div>'
    
    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    
    if count > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
