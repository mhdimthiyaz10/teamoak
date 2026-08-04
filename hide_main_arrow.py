import os
import glob
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

hide_arrow_style = """
<style>
/* Hide main nav arrow (v) for both nav-links and hero-nav-links globally */
.nav-links li.has-arrow > a::after,
.hero-nav-links li.has-arrow > a::after {
    display: none !important;
    content: none !important;
}
</style>
</head>"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Expand MEGA MENU OVERRIDE V5 to also include .hero-nav-links if not already done
    if ".nav-links li.has-arrow .dropdown {" in content and ".nav-links li.has-arrow, .hero-nav-links li.has-arrow" not in content:
        content = re.sub(
            r"\.nav-links\s+li\.has-arrow",
            r".nav-links li.has-arrow, .hero-nav-links li.has-arrow",
            content
        )
        modified = True
        
    if "/* Hide main nav arrow (v) for both nav-links and hero-nav-links globally */" not in content:
        content = content.replace("</head>", hide_arrow_style)
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
