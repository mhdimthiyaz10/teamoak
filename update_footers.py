import os
import re

footer_html = '''    <!-- STANDARDIZED FOOTER -->
    <footer class="global-footer">
        <div class="gf-inner">
            <div class="gf-col gf-brand">
                <img src="assets/logo.png.png" alt="Team OAK" class="gf-logo-img">
                <p class="gf-tagline">BUILDING EXCELLENCE ACROSS INDUSTRIES</p>
            </div>
            <div class="gf-col gf-links">
                <h4>QUICK LINKS</h4>
                <div class="gf-line"></div>
                <ul>
                    <li><a href="about.html">About</a></li>
                    <li><a href="index.html#companies">Companies</a></li>
                    <li><a href="index.html#services">Services</a></li>
                </ul>
            </div>
            <div class="gf-col gf-contact">
                <h4>CONTACT INFO</h4>
                <div class="gf-line"></div>
                <p>123 Corporate Blvd, Suite 800</p>
                <p><a href="mailto:contact@teamoak.com">contact@teamoak.com</a></p>
                <p>+1 (800) 123-4567</p>
            </div>
        </div>
        <div class="gf-bottom">
            <p>&copy; 2026 Team OAK. All Rights Reserved.</p>
        </div>
    </footer>'''

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace everything from <footer to </footer>
    new_content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL | re.IGNORECASE)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated footer in {f}')
