import os
import glob
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

final_fix_code = """
<!-- MENU SHIFT RIGHT FIX -->
<style>
@media (max-width: 768px) {
    /* Moderate indentation to preserve screen real estate */
    .nav-links li.has-arrow .dropdown,
    .hero-nav-links li.has-arrow .dropdown,
    .nav-links li.has-arrow.open .dropdown,
    .hero-nav-links li.has-arrow.open .dropdown {
        margin-left: 15px !important;
        width: calc(100% - 15px) !important;
        transform: none !important; /* FIX THE -50% TRANSLATE WHEN OPEN */
        left: 0 !important;
    }
    
    .nav-links li.has-arrow .dropdown > li > a,
    .hero-nav-links li.has-arrow .dropdown > li > a {
        padding-left: 1rem !important;
        white-space: normal !important; /* ALLOW TEXT TO WRAP */
        line-height: 1.4 !important;
    }
    
    /* Moderate indentation for nested flyout */
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout,
    .nav-links li.has-arrow .dropdown > li.has-flyout.open .flyout,
    .hero-nav-links li.has-arrow .dropdown > li.has-flyout.open .flyout {
        margin-left: 15px !important;
        width: calc(100% - 15px) !important;
        transform: none !important;
        left: 0 !important;
    }
    
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout li a,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {
        padding-left: 1.5rem !important;
        white-space: normal !important; /* ALLOW TEXT TO WRAP */
        line-height: 1.4 !important;
        font-size: 0.85rem !important;
    }
}
</style>
<!-- END MENU SHIFT RIGHT FIX -->
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Replace the existing MENU SHIFT RIGHT FIX block entirely
    pattern = r'<!-- MENU SHIFT RIGHT FIX -->.*?<!-- END MENU SHIFT RIGHT FIX -->'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, final_fix_code.strip(), content, flags=re.DOTALL)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
