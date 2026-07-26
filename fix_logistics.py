import os
import glob

html_files = glob.glob('*.html')
logistics_item = '                            <li><a href="team-oak-logistics.html">Team Oak Logistics Services</a></li>\n'

updated_files = []
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    added = False
    for i, line in enumerate(lines):
        new_lines.append(line)
        if 'oak-academy-of-design.html' in line:
            # Check if logistics is already on the next line
            if i + 1 < len(lines) and 'team-oak-logistics.html' not in lines[i+1]:
                new_lines.append(logistics_item)
                added = True
    
    if added:
        with open(file, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        updated_files.append(file)

print(f"Updated files: {updated_files}")
