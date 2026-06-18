import os

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
source_file = os.path.join(directory, "wymax-media.html")
target_file = os.path.join(directory, "team-oak-builders.html")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements to turn it into Team Oak Builders & Developers
replacements = {
    '<title>Wymax Media | Team Oak</title>': '<title>Team Oak Builders &amp; Developers | Team Oak</title>',
    '<meta name="description" content="Wymax Media is a creative and performance-driven digital marketing agency committed to helping businesses build a powerful digital presence.">': '<meta name="description" content="Team Oak Builders & Developers is a premier construction and real estate development company dedicated to shaping the future with innovative and sustainable projects.">',
    "url('assets/wymax_media_bg.png')": "url('assets/team_oak_builders_bg.png')",
    '<span class="page-eyebrow fu">Media & Digital Solutions</span>': '<span class="page-eyebrow fu">Construction & Development</span>',
    '<h1 class="fu d1">WYMAX<br><em>MEDIA</em></h1>': '<h1 class="fu d1">Team Oak<br><em>Builders &amp; Developers</em></h1>',
    
    # We will replace the entire content section inside the story block.
    # The current one has "A Performance-Driven Digital Agency"
}

for old_text, new_text in replacements.items():
    content = content.replace(old_text, new_text)

# We replace the specific text block. We will just use regex to replace everything inside the <div class="story-text">
import re

new_story_text = '''<div class="story-text">
                    <h2 class="fu" style="font-family: 'Outfit', sans-serif; text-align: left; font-size: 2.2rem; color: #ffffff; margin-bottom: 2rem;">Building the Future Together</h2>
                    
                    <p class="fu d1" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; line-height: 2; color: #cccccc; text-align: justify;">
                        <strong>Team Oak Builders &amp; Developers</strong> is a premier construction and real estate development company dedicated to shaping the future with innovative, sustainable, and high-quality projects.
                    </p>
                    
                    <p class="fu d2" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; line-height: 2; color: #cccccc; text-align: justify;">
                        With a steadfast commitment to excellence, we specialize in delivering state-of-the-art commercial, residential, and industrial developments that meet the evolving needs of our modern society. Our team of expert engineers, architects, and project managers work closely with clients to turn visions into reality.
                    </p>

                    <div class="highlight-quote fu" style="font-family: 'Outfit', sans-serif; font-weight: 300; border-color: #c59b27; color: #e0e0e0; font-size: 1.45rem; text-align: left;">
                        "We don't just construct buildings; we create landmark destinations that inspire, endure, and elevate the standard of living for generations to come."
                    </div>

                    <p class="fu d1" style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.15rem; line-height: 2; color: #cccccc; text-align: justify;">
                        From initial concept and architectural design through to final construction and property management, Team Oak Builders &amp; Developers provides comprehensive end-to-end solutions, ensuring every project is delivered on time, within budget, and to the highest standards of safety and quality.
                    </p>
                </div>'''

content = re.sub(r'<div class="story-text">.*?</div>\s*</div>\s*</div>\s*</section>', 
                 new_story_text + '\n            </div>\n        </div>\n    </section>', 
                 content, flags=re.DOTALL)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully created team-oak-builders.html")
