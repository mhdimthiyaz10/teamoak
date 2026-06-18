import os

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
source_file = os.path.join(directory, "general-trading.html")
target_file = os.path.join(directory, "makin-spare-parts-trading.html")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "<title>Team Oak General Trading Company</title>": "<title>Makin Spare parts Trading Company</title>",
    '<span class="page-eyebrow fu">Building Materials</span>': '<span class="page-eyebrow fu">Spare Parts Trading</span>',
    '<h1 class="fu d1">Team Oak<br><em>General Trading Company</em></h1>': '<h1 class="fu d1">Makin Spare parts<br><em>Trading Company</em></h1>',
    '<h2 class="fu">Comprehensive Construction Solutions</h2>': '<h2 class="fu">Premium Spare Parts Solutions</h2>',
    'At Team Oak Building Materials, we are committed to being your trusted source for high-quality building materials and construction solutions.': 'At Makin Spare parts Trading Company, we are committed to being your trusted source for high-quality spare parts and industrial solutions.',
    'Based in Saudi Arabia, our firm specializes in providing a comprehensive range of products designed to meet the diverse needs of construction projects, from residential to commercial.': 'Our firm specializes in providing a comprehensive range of genuine and aftermarket spare parts designed to meet the diverse needs of various industries.',
    'Our extensive inventory includes everything from structural steel and concrete to finishing materials and innovative building solutions.': 'Our extensive inventory includes everything from critical engine components and mechanical parts to specialized industrial equipment.',
    'Whether you are working on a large-scale development or a smaller renovation, Team Oak Building Materials is equipped to support you every step of the way.': 'Whether you are maintaining a large fleet or require specific components for specialized machinery, Makin Spare parts Trading Company is equipped to support you every step of the way.'
}

for old_text, new_text in replacements.items():
    content = content.replace(old_text, new_text)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully created makin-spare-parts-trading.html")
