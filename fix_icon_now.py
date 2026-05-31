import os
import glob

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
        position: relative !important;
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

    if '<!-- MOBILE ICON POSITION FIX -->' not in content:
        # We will append it to the end of the file right before </html> if possible, or just string replace </body>
        if '</body>' in content:
            new_content = content.replace('</body>', absolute_position_code + '\n</body>')
        elif '</BODY>' in content:
            new_content = content.replace('</BODY>', absolute_position_code + '\n</BODY>')
        else:
            new_content = content + '\n' + absolute_position_code
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
