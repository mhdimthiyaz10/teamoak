import os
import glob
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

nav_target = '<li><a href="oak-academy-of-design.html">Oak Academy of Design</a></li>'
nav_addition = '\n                            <li><a href="team-oak-logistics.html">Team Oak Logistics Services</a></li>'

footer_target = '<li><a href="bubbl.html">Bubbl</a></li>'
footer_addition = '\n                        <li><a href="team-oak-logistics.html">Logistics Services</a></li>'

for filepath in html_files:
    if os.path.basename(filepath) == 'team-oak-logistics.html':
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    
    # 1. Main navigation
    if nav_target in content and 'team-oak-logistics.html' not in content:
        content = content.replace(nav_target, nav_target + nav_addition)
        modified = True
    elif '<li><a href="team-oak-builders.html">Team Oak Builders &amp; Developers</a></li>' in content and 'team-oak-logistics.html' not in content:
        # Fallback if oak-academy-of-design is missing
        fallback_target = '<li><a href="team-oak-builders.html">Team Oak Builders &amp; Developers</a></li>'
        content = content.replace(fallback_target, fallback_target + nav_addition)
        modified = True

    # 2. Footer navigation
    if footer_target in content and 'team-oak-logistics.html' not in content:
        content = content.replace(footer_target, footer_target + footer_addition)
        modified = True

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")

# 3. Create the new page
source_file = os.path.join(directory, "team-oak-transport.html")
target_file = os.path.join(directory, "team-oak-logistics.html")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '<title>Team Oak Transport | Team Oak</title>': '<title>Team Oak Logistics Services | Team Oak</title>',
    '<meta name="description" content="Team Oak Transport & Heavy Equipment Rental LLC">': '<meta name="description" content="Team Oak Logistics Services provides seamless and efficient supply chain solutions.">',
    "url('assets/team-oak-transport-bg.png')": "url('assets/trading-bg.png')", # Using an existing image, user can change later
    '<span class="page-eyebrow fu">Logistics & Heavy Equipment</span>': '<span class="page-eyebrow fu">Global Supply Chain & Freight</span>',
    '<h1 class="fu d1">Team Oak Transport<br><em>& Heavy Equipment Rental</em></h1>': '<h1 class="fu d1">Team Oak<br><em>Logistics Services</em></h1>',
}

for old_text, new_text in replacements.items():
    content = content.replace(old_text, new_text)

new_story_text = '''<div class="story-text">
                    <h2 class="fu">Seamless Logistics & Supply Chain Solutions</h2>
                    <p class="fu d1">Team Oak Logistics Services is a premier logistics provider dedicated to optimizing your supply chain. We offer a comprehensive suite of services including freight forwarding, warehousing, distribution, and custom clearance, ensuring that your goods reach their destination safely, on time, and within budget.</p>
                    
                    <p class="fu d2">Leveraging advanced tracking technology and a robust global network, our team of logistics experts is capable of handling complex transportation challenges across various industries. Whether by land, sea, or air, we tailor our solutions to meet your unique business requirements, minimizing downtime and maximizing efficiency.</p>

                    <div class="highlight-quote fu">
                        "At Team Oak Logistics Services, we don't just move cargo; we deliver reliability, transparency, and a commitment to driving your business forward."
                    </div>
                </div>'''

content = re.sub(r'<div class="story-text">.*?</div>\s*</div>\s*</div>\s*</section>', 
                 new_story_text + '\n            </div>\n        </div>\n    </section>', 
                 content, flags=re.DOTALL)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully created team-oak-logistics.html")
