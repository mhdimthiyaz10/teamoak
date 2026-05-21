import os
import re

footer_html = '''    <!-- MINIMAL STANDARD FOOTER -->
    <svg style="display:none;">
        <symbol id="icon-phone" viewBox="0 0 24 24">
            <path fill="currentColor" d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/>
        </symbol>
        <symbol id="icon-location" viewBox="0 0 24 24">
            <path fill="currentColor" d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z"/>
        </symbol>
        <symbol id="icon-email" viewBox="0 0 24 24">
            <path fill="currentColor" d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/>
        </symbol>
    </svg>
    <footer class="minimal-footer">
        <div class="mf-container">
            <div class="mf-columns">
                <div class="mf-col mf-contact">
                    <h4>Contact</h4>
                    <ul>
                        <li class="mf-contact-item">
                            <div class="mf-icon"><svg><use href="#icon-phone"></use></svg></div>
                            <div class="mf-text">+1 (800) 123-4567</div>
                        </li>
                        <li class="mf-contact-item">
                            <div class="mf-icon"><svg><use href="#icon-location"></use></svg></div>
                            <div class="mf-text">123 Corporate Blvd, Suite 800<br>Business District, London</div>
                        </li>
                        <li class="mf-contact-item">
                            <div class="mf-icon"><svg><use href="#icon-email"></use></svg></div>
                            <div class="mf-text">contact@teamoak.com</div>
                        </li>
                    </ul>
                </div>
                
                <div class="mf-col">
                    <h4>Navigate</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="about.html">About Us</a></li>
                        <li><a href="media.html">Media</a></li>
                        <li><a href="career.html">Career</a></li>
                        <li><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>

                <div class="mf-col">
                    <h4>Trading &amp; Industry</h4>
                    <ul>
                        <li><a href="tobacco-trading.html">Tobacco Trading</a></li>
                        <li><a href="food-stuff-trading.html">Food Stuff Trading</a></li>
                        <li><a href="kizhisseri-jewellers.html">Kizhissery Jewellers</a></li>
                        <li><a href="general-trading.html">General Trading</a></li>
                        <li><a href="sugar-packing.html">Sugar Packing</a></li>
                    </ul>
                </div>

                <div class="mf-col">
                    <h4>Services</h4>
                    <ul>
                        <li><a href="best-vibes-contracting.html">Contracting LLC</a></li>
                        <li><a href="team-oak-hotels.html">Hotels &amp; Apartments</a></li>
                        <li><a href="team-oak-camps.html">Resort Camps</a></li>
                        <li><a href="mamichi-apartments.html">Mamichi Apartments</a></li>
                        <li><a href="oak-architects.html">Oak Architects</a></li>
                        <li><a href="bubbl.html">Bubbl</a></li>
                    </ul>
                </div>

                <div class="mf-col">
                    <h4>Follow Us</h4>
                    <ul>
                        <li><a href="#">Facebook</a></li>
                        <li><a href="#">Instagram</a></li>
                        <li><a href="#">LinkedIn</a></li>
                        <li><a href="#">Twitter</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="mf-bottom">
                <div class="mf-copy">&copy; Copyright Team OAK. All rights reserved. 2026</div>
                <div class="mf-legal">
                    <a href="#">Privacy &amp; Policy</a>
                    <a href="#">Terms &amp; Condition</a>
                </div>
            </div>
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
