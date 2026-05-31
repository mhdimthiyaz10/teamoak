import os
import glob
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

final_fix_code = """
<!-- MENU SHIFT RIGHT FIX -->
<style>
@media (max-width: 768px) {
    /* Push the main dropdown heavily to the right */
    .nav-links li.has-arrow .dropdown,
    .hero-nav-links li.has-arrow .dropdown,
    .nav-links li.has-arrow.open .dropdown,
    .hero-nav-links li.has-arrow.open .dropdown {
        margin-left: 35px !important;
        width: calc(100% - 35px) !important;
        transform: none !important; /* FIX THE -50% TRANSLATE WHEN OPEN */
        left: 0 !important;
        box-sizing: border-box !important;
    }
    
    .nav-links li.has-arrow .dropdown > li > a,
    .hero-nav-links li.has-arrow .dropdown > li > a {
        padding-left: 2rem !important; /* Indent the text further right */
        white-space: normal !important; 
        line-height: 1.5 !important;
    }
    
    /* Push the nested flyout further right */
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout,
    .nav-links li.has-arrow .dropdown > li.has-flyout.open .flyout,
    .hero-nav-links li.has-arrow .dropdown > li.has-flyout.open .flyout {
        margin-left: 35px !important;
        width: calc(100% - 35px) !important;
        transform: none !important;
        left: 0 !important;
        box-sizing: border-box !important;
    }
    
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout li a,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {
        padding-left: 2rem !important; /* Indent nested text further right */
        white-space: normal !important; 
        line-height: 1.5 !important;
        font-size: 0.85rem !important;
    }
}
</style>
<!-- END MENU SHIFT RIGHT FIX -->

<!-- MOBILE ICON POSITION FIX -->
<style>
@media (max-width: 768px) {
    .mobile-menu-btn {
        position: absolute !important;
        right: 15px !important;
        top: 50% !important;
        transform: translateY(-50%) !important;
    }
    .hero-nav-container, .nav {
        position: relative !important;
    }
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
    
    # Remove old ICON position block if present
    content = re.sub(r'<!-- MOBILE ICON POSITION FIX -->.*?<!-- END MOBILE ICON POSITION FIX -->', '', content, flags=re.DOTALL)
    
    # Replace the existing MENU SHIFT RIGHT FIX block entirely
    pattern = r'<!-- MENU SHIFT RIGHT FIX -->.*?<!-- END MENU SHIFT RIGHT FIX -->'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, final_fix_code.strip(), content, flags=re.DOTALL)
    else:
        # Just append before </body>
        if '</body>' in content:
            content = content.replace('</body>', final_fix_code + '\n</body>')
        else:
            content += '\n' + final_fix_code
            
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
