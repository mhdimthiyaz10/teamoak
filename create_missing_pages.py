import os
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
source_file = os.path.join(directory, "wymax-media.html")

def create_page(filename, title, eyebrow, heading_em, desc):
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements
    replacements = {
        '<title>Wymax Media | Team Oak</title>': f'<title>{title} | Team Oak</title>',
        '<meta name="description" content="Wymax Media is a creative and performance-driven digital marketing agency committed to helping businesses build a powerful digital presence.">': f'<meta name="description" content="{desc}">',
        "url('assets/wymax_media_bg.png')": "url('assets/contact-bg.png')",
        '<span class="page-eyebrow fu">Media & Digital Solutions</span>': f'<span class="page-eyebrow fu">{eyebrow}</span>',
        '<h1 class="fu d1">WYMAX<br><em>MEDIA</em></h1>': f'<h1 class="fu d1">Team Oak<br><em>{heading_em}</em></h1>',
    }

    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)

    new_story_text = f'''<div class="story-text">
                    <h2 class="fu" style="font-family: 'Outfit', sans-serif; text-align: left; font-size: 2.2rem; color: #ffffff; margin-bottom: 2rem;">Welcome to {title}</h2>
                    
                    <p class="fu d1" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; line-height: 2; color: #cccccc; text-align: justify;">
                        This section is currently under development. Please check back later for updates regarding our {heading_em}.
                    </p>
                </div>'''

    content = re.sub(r'<div class="story-text">.*?</div>\s*</div>\s*</div>\s*</section>', 
                     new_story_text + '\n            </div>\n        </div>\n    </section>', 
                     content, flags=re.DOTALL)

    target_file = os.path.join(directory, filename)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {filename}")

create_page("our-ventures.html", "Our Ventures", "Explore Our Portfolio", "Ventures", "Explore the diverse portfolio of ventures under the Team Oak umbrella.")
create_page("our-clients.html", "Our Clients", "Global Partnerships", "Clients", "Discover the prestigious clients and partners who trust Team Oak.")
