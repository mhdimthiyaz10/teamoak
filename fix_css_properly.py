import os
import glob
import re

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(directory, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    
    # Revert the bad regex replacement
    # I replaced `.nav-links li.has-arrow` with `.nav-links li.has-arrow, .hero-nav-links li.has-arrow`
    # Let's revert that and do it properly.
    
    if ".nav-links li.has-arrow, .hero-nav-links li.has-arrow" in content:
        # Revert back to `.nav-links li.has-arrow`
        content = content.replace(".nav-links li.has-arrow, .hero-nav-links li.has-arrow", ".nav-links li.has-arrow")
        modified = True
        
    # Now, let's properly add the .hero-nav-links variations
    # Instead of doing complex regex, let's just duplicate the entire block for .hero-nav-links
    # Wait, the Mega Menu block has many rules.
    # It's safer to just inject a <style> block that applies all the Mega Menu styles to .hero-nav-links
    # Actually, if I just do a carefully crafted regex to replace:
    # `.nav-links li.has-arrow .dropdown` -> `.nav-links li.has-arrow .dropdown, .hero-nav-links li.has-arrow .dropdown`
    # `.nav-links li.has-arrow.open .dropdown` -> `.nav-links li.has-arrow.open .dropdown, .hero-nav-links li.has-arrow.open .dropdown`
    # And so on.
    
    if ".nav-links li.has-arrow .dropdown {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown {", ".nav-links li.has-arrow .dropdown, .hero-nav-links li.has-arrow .dropdown {")
        modified = True
    if ".nav-links li.has-arrow.open .dropdown {" in content:
        content = content.replace(".nav-links li.has-arrow.open .dropdown {", ".nav-links li.has-arrow.open .dropdown, .hero-nav-links li.has-arrow.open .dropdown {")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li > a {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li > a {", ".nav-links li.has-arrow .dropdown > li > a, .hero-nav-links li.has-arrow .dropdown > li > a {")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li > a::after {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li > a::after {", ".nav-links li.has-arrow .dropdown > li > a::after, .hero-nav-links li.has-arrow .dropdown > li > a::after {")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li > a:hover," in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li > a:hover,", ".nav-links li.has-arrow .dropdown > li > a:hover, .hero-nav-links li.has-arrow .dropdown > li > a:hover,")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li.active > a," in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li.active > a,", ".nav-links li.has-arrow .dropdown > li.active > a, .hero-nav-links li.has-arrow .dropdown > li.active > a,")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li:hover > a {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li:hover > a {", ".nav-links li.has-arrow .dropdown > li:hover > a, .hero-nav-links li.has-arrow .dropdown > li:hover > a {")
        modified = True
    if ".nav-links li.has-arrow .dropdown li.has-flyout .flyout {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown li.has-flyout .flyout {", ".nav-links li.has-arrow .dropdown li.has-flyout .flyout, .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout {")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li.has-flyout:first-child .flyout {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li.has-flyout:first-child .flyout {", ".nav-links li.has-arrow .dropdown > li.has-flyout:first-child .flyout, .hero-nav-links li.has-arrow .dropdown > li.has-flyout:first-child .flyout {")
        modified = True
    if ".nav-links li.has-arrow .dropdown:hover > li.has-flyout:first-child:not(:hover) .flyout {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown:hover > li.has-flyout:first-child:not(:hover) .flyout {", ".nav-links li.has-arrow .dropdown:hover > li.has-flyout:first-child:not(:hover) .flyout, .hero-nav-links li.has-arrow .dropdown:hover > li.has-flyout:first-child:not(:hover) .flyout {")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li.has-flyout:hover .flyout," in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li.has-flyout:hover .flyout,", ".nav-links li.has-arrow .dropdown > li.has-flyout:hover .flyout, .hero-nav-links li.has-arrow .dropdown > li.has-flyout:hover .flyout,")
        modified = True
    if ".nav-links li.has-arrow .dropdown > li.has-flyout.active .flyout {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown > li.has-flyout.active .flyout {", ".nav-links li.has-arrow .dropdown > li.has-flyout.active .flyout, .hero-nav-links li.has-arrow .dropdown > li.has-flyout.active .flyout {")
        modified = True
    if ".nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {", ".nav-links li.has-arrow .dropdown li.has-flyout .flyout li a, .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {")
        modified = True
    if ".nav-links li.has-arrow .dropdown li.has-flyout .flyout li a:hover {" in content:
        content = content.replace(".nav-links li.has-arrow .dropdown li.has-flyout .flyout li a:hover {", ".nav-links li.has-arrow .dropdown li.has-flyout .flyout li a:hover, .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout li a:hover {")
        modified = True
        
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
