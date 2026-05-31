import os
import glob
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

absolute_position_code = """
<!-- MOBILE ICON POSITION FIX -->
<style>
@media (max-width: 768px) {
    .mobile-menu-btn {
        position: absolute !important;
        right: 15px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
    }
    
    /* Ensure the parent nav containers are positioned relatively */
    .hero-nav-container, .nav {
        position: relative;
    }
    
    /* When active, the rotation transform needs to combine with the translateY */
    .mobile-menu-btn.active span:nth-child(1) { transform: translateY(8px) rotate(45deg) !important; }
    .mobile-menu-btn.active span:nth-child(2) { opacity: 0 !important; }
    .mobile-menu-btn.active span:nth-child(3) { transform: translateY(-8px) rotate(-45deg) !important; }
}
</style>
<!-- END MOBILE ICON POSITION FIX -->
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    if '<!-- MOBILE ICON POSITION FIX -->' not in content:
        # inject right before </body>
        new_content = content.replace('</body>', absolute_position_code + '\n</body>')
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")
