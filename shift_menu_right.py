import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

shift_code = """
<!-- MENU SHIFT RIGHT FIX -->
<style>
@media (max-width: 768px) {
    /* Push the entire dropdown panel to the right */
    .nav-links li.has-arrow .dropdown,
    .hero-nav-links li.has-arrow .dropdown {
        margin-left: 30px !important;
        width: calc(100% - 30px) !important;
    }
    
    /* Ensure the text has plenty of left padding so it's never cut off */
    .nav-links li.has-arrow .dropdown > li > a,
    .hero-nav-links li.has-arrow .dropdown > li > a {
        padding-left: 1.5rem !important;
    }
    
    /* Push the nested flyout panel further right as well */
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout {
        margin-left: 20px !important;
        width: calc(100% - 20px) !important;
    }
    
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout li a,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {
        padding-left: 1rem !important;
    }
}
</style>
<!-- END MENU SHIFT RIGHT FIX -->
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- MENU SHIFT RIGHT FIX -->' not in content:
        # inject right before </body>
        new_content = content.replace('</body>', shift_code + '\n</body>')
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")
