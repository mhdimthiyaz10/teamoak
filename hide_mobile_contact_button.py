import os
import glob
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

hidden_contact_button_code = """
<!-- MOBILE CONTACT BUTTON FIX -->
<style>
@media (max-width: 768px) {
    .nav-btn, .hero-nav-cta {
        display: none !important;
    }
}
</style>
<!-- END MOBILE CONTACT BUTTON FIX -->
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # Replace the existing MOBILE CONTACT BUTTON FIX block entirely
    pattern = r'<!-- MOBILE CONTACT BUTTON FIX -->.*?<!-- END MOBILE CONTACT BUTTON FIX -->'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, hidden_contact_button_code.strip(), content, flags=re.DOTALL)
    else:
        # Just in case it wasn't there, we can append it, but we know it's there
        content = content.replace('</body>', hidden_contact_button_code + '\n</body>')
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
