import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

override_code = """
<!-- MOBILE MENU CUTOFF FIX -->
<style>
@media (max-width: 768px) {
    .nav-links li.has-arrow .dropdown,
    .hero-nav-links li.has-arrow .dropdown {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        box-sizing: border-box !important;
        transform: none !important;
        left: 0 !important;
        right: auto !important;
    }
    .nav-links li.has-arrow .dropdown > li > a,
    .hero-nav-links li.has-arrow .dropdown > li > a {
        padding: 1rem 1rem !important;
        margin: 0 !important;
        box-sizing: border-box !important;
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        transform: none !important;
        position: relative !important;
        left: 0 !important;
    }
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout {
        padding: 0 !important;
        margin: 0 !important;
        box-sizing: border-box !important;
        width: 100% !important;
        transform: none !important;
        left: 0 !important;
        right: auto !important;
        background: rgba(255, 255, 255, 0.05) !important;
    }
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout li a,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {
        padding: 0.8rem 1rem 0.8rem 2rem !important;
        margin: 0 !important;
        box-sizing: border-box !important;
        justify-content: flex-start !important;
        text-align: left !important;
        width: 100% !important;
        transform: none !important;
        position: relative !important;
        left: 0 !important;
    }
}
</style>
<!-- END MOBILE MENU CUTOFF FIX -->
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- MOBILE MENU CUTOFF FIX -->' not in content:
        # inject right before </body>
        new_content = content.replace('</body>', override_code + '\n</body>')
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")
