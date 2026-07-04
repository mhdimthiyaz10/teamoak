import os
import re
import glob

# 1. Extract the perfect footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# We look for the marker or svg
start_idx = index_content.find('<svg style="display:none;">\n        <symbol id="icon-phone"')
if start_idx == -1:
    start_idx = index_content.find('<svg style="display:none;">')

end_idx = index_content.find('</footer>', start_idx)
if start_idx == -1 or end_idx == -1:
    print("Could not find footer in index.html")
    exit(1)

# Include the closing tag
end_idx += len('</footer>')
footer_content = index_content[start_idx:end_idx]

# Let's also prepend the <!-- MINIMAL STANDARD FOOTER --> comment just in case
footer_content = "<!-- MINIMAL STANDARD FOOTER -->\n    " + footer_content

html_files = glob.glob('*.html')

for file in html_files:
    if file == 'index.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Try to find existing <svg style="display:none;"> and replace from there to </footer>
    svg_start = content.find('<svg style="display:none;">\n        <symbol id="icon-phone"')
    if svg_start == -1:
        svg_start = content.find('<svg style="display:none;">')
        
    if svg_start != -1:
        f_end_idx = content.find('</footer>', svg_start)
        if f_end_idx != -1:
            # Replace the whole block
            new_content = content[:svg_start] + footer_content + content[f_end_idx + len('</footer>'):]
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated footer (SVG+Footer block) in {file}")
            continue
            
    # If no SVG, just replace <footer ...> ... </footer>
    new_content = re.sub(r'<footer.*?</footer>', footer_content, content, flags=re.DOTALL | re.IGNORECASE)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer (Regex match) in {file}")
    else:
        print(f"Could not find a footer to replace in {file}")

print("Finished updating all footers.")
