import os
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
filepath = os.path.join(directory, "index.html")

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Expand `.nav-links` to `.nav-links, .hero-nav-links` in MEGA MENU OVERRIDE V5 block
# But be careful not to match `.hero-nav-links` if it's already there
new_content = re.sub(
    r"\.nav-links\s+li\.has-arrow",
    r".nav-links li.has-arrow, .hero-nav-links li.has-arrow",
    content
)

# 2. Hide the main arrow (the `v` chevron next to "What We Do") globally in index.html
# Find the inline style that hides `.nav-links li.has-arrow > a::after`
hide_arrow_style = """
        /* Hide main nav arrow */
        .nav-links li.has-arrow > a::after,
        .hero-nav-links li.has-arrow > a::after {
            display: none !important;
            content: none !important;
        }
"""
if "/* Hide main nav arrow */" in new_content:
    new_content = re.sub(
        r"/\*\s*Hide main nav arrow\s*\*/[\s\S]*?\}",
        hide_arrow_style.strip(),
        new_content
    )

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print(f"Updated {os.path.basename(filepath)}")
