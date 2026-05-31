import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

override_code = """
<!-- MOBILE MENU WIDTH FIX -->
<style>
@media (max-width: 768px) {
    .nav-links, .hero-nav-links {
        width: 100% !important;
        max-width: 100% !important;
    }
}
</style>
<!-- END MOBILE MENU WIDTH FIX -->
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We can just append the override block
    if '<!-- MOBILE MENU WIDTH FIX -->' not in content:
        # inject right before </body>
        new_content = content.replace('</body>', override_code + '\n</body>')
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")
