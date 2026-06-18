import os
import glob
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

nav_target = '<li><a href="team-oak-builders.html">Team Oak Builders &amp; Developers</a></li>'
nav_addition = '\n                            <li><a href="oak-academy-of-design.html">Oak Academy of Design</a></li>'

for filepath in html_files:
    # Skip the new file if it somehow exists already
    if os.path.basename(filepath) == 'oak-academy-of-design.html':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # 1. Main navigation
    if nav_target in content and 'oak-academy-of-design.html' not in content:
        content = content.replace(nav_target, nav_target + nav_addition)
        modified = True
    elif '<li><a href="pharma-fleet.html">Pharma Fleet</a></li>' in content and 'oak-academy-of-design.html' not in content:
        # Fallback
        content = content.replace('<li><a href="pharma-fleet.html">Pharma Fleet</a></li>', 
                                  '<li><a href="pharma-fleet.html">Pharma Fleet</a></li>' + nav_addition)
        modified = True

    # 2. Footer navigation
    # We want to add it to the "Services" list in the footer.
    if 'oak-academy-of-design.html' not in content:
        match = re.search(r'(<h4>Services</h4>\s*<ul>.*?)(</ul>)', content, flags=re.DOTALL)
        if match:
            new_block = match.group(1) + '    <li><a href="oak-academy-of-design.html">Oak Academy of Design</a></li>\n                    ' + match.group(2)
            content = content.replace(match.group(0), new_block)
            modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

# 3. Create the new page
source_file = os.path.join(directory, "team-oak-builders.html")
target_file = os.path.join(directory, "oak-academy-of-design.html")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<title>Team Oak Builders &amp; Developers | Team Oak</title>': '<title>Oak Academy of Design | Team Oak</title>',
    '<meta name="description" content="Team Oak Builders & Developers is a premier construction and real estate development company dedicated to shaping the future with innovative and sustainable projects.">': '<meta name="description" content="Oak Academy of Design is a premier institution dedicated to nurturing the next generation of creative minds in architecture and design.">',
    "url('assets/team_oak_builders_bg2.png')": "url('assets/oak_academy_bg.png')",
    '<span class="page-eyebrow fu">Construction & Development</span>': '<span class="page-eyebrow fu">Education & Creativity</span>',
    '<h1 class="fu d1">Team Oak<br><em>Builders &amp; Developers</em></h1>': '<h1 class="fu d1">Oak Academy<br><em>of Design</em></h1>',
}

for old_text, new_text in replacements.items():
    content = content.replace(old_text, new_text)

new_story_text = '''<div class="story-text">
                    <h2 class="fu" style="font-family: 'Outfit', sans-serif; text-align: left; font-size: 2.2rem; color: #ffffff; margin-bottom: 2rem;">Nurturing Creative Excellence</h2>
                    
                    <p class="fu d1" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; line-height: 2; color: #cccccc; text-align: justify;">
                        <strong>Oak Academy of Design</strong> is an elite educational institution committed to inspiring and equipping the next generation of creative professionals in the fields of architecture, interior design, and creative arts.
                    </p>
                    
                    <p class="fu d2" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; line-height: 2; color: #cccccc; text-align: justify;">
                        Our curriculum blends rigorous academic theory with practical, hands-on studio experience, guided by industry-leading professionals. We foster an environment of innovation, encouraging students to challenge conventions and redefine the boundaries of modern design.
                    </p>

                    <div class="highlight-quote fu" style="font-family: 'Outfit', sans-serif; font-weight: 300; border-color: #c59b27; color: #e0e0e0; font-size: 1.45rem; text-align: left;">
                        "At Oak Academy of Design, we don't just teach principles; we cultivate visionaries who will shape the aesthetic and functional future of our built environment."
                    </div>

                    <p class="fu d1" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; line-height: 2; color: #cccccc; text-align: justify;">
                        With state-of-the-art facilities, comprehensive mentorship programs, and a dynamic creative community, the Academy provides the perfect launchpad for students aspiring to make a profound impact in the global design landscape.
                    </p>
                </div>'''

content = re.sub(r'<div class="story-text">.*?</div>\s*</div>\s*</div>\s*</section>', 
                 new_story_text + '\n            </div>\n        </div>\n    </section>', 
                 content, flags=re.DOTALL)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully created oak-academy-of-design.html")

