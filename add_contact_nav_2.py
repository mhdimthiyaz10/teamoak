import os
import glob
import re

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # We want to find the Career link that is right before the closing </ul> of the navbar
    # and the Contact Us button.
    # Pattern: <li><a href="career.html"[^>]*>Career</a></li> ... </ul> ... <a href="contact.html" class="...nav-btn|hero-nav-cta..."
    
    pattern2 = r'(<li><a href="career.html"[^>]*>Career</a></li>\s*)</ul>(\s*(?:<!--.*?-->\s*)?<a href="contact.html"[^>]*>)'
    replacement2 = r'\1<li class="mobile-contact"><a href="contact.html">Contact Us</a></li>\n        </ul>\2'
    
    # If the file already has mobile-contact, we don't replace it again
    if '<li class="mobile-contact">' not in content:
        content = re.sub(pattern2, replacement2, content)

    css_injection = """
<style>
/* Hide contact us in nav list on desktop, show on mobile */
.mobile-contact { display: none !important; }
@media (max-width: 768px) {
    .mobile-contact { display: block !important; }
}
</style>
"""
    if '<li class="mobile-contact">' in content and '/* Hide contact us in nav list on desktop' not in content:
        content = content.replace('</head>', css_injection + '</head>')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
