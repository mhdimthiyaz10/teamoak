import os
import re

footer_html = '''    <!-- MINIMAL STANDARD FOOTER -->
    <svg style="display:none;">
        <symbol id="icon-phone" viewbox="0 0 24 24">
            <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 00-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z" fill="currentColor"></path>
        </symbol>
        <symbol id="icon-location" viewbox="0 0 24 24">
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 010-5 2.5 2.5 0 010 5z" fill="currentColor"></path>
        </symbol>
        <symbol id="icon-email" viewbox="0 0 24 24">
            <path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="currentColor"></path>
        </symbol>
    </svg>
    <footer class="minimal-footer">
        <style>
            .custom-footer-grid {
                grid-template-columns: 1.8fr 1.2fr 4.5fr 1fr !important;
            }
            .ventures-grid {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1.5rem;
            }
            @media (max-width: 1024px) {
                .custom-footer-grid { grid-template-columns: 1fr 1fr 1fr !important; }
                .ventures-grid { grid-column: 1 / -1; margin-top: 1rem; }
            }
            @media (max-width: 768px) {
                .ventures-grid { grid-template-columns: 1fr 1fr; }
            }
            @media (max-width: 480px) {
                .custom-footer-grid { grid-template-columns: 1fr !important; }
                .ventures-grid { grid-template-columns: 1fr; }
            }
        </style>
        <div class="mf-container">
            <div class="mf-columns custom-footer-grid">
                <div class="mf-col mf-contact">
                    <h4 data-i18n="global_contact">Contact</h4>
                    <ul>
                        <li class="mf-contact-item">
                            <div class="mf-icon"><svg><use href="#icon-phone"></use></svg></div>
                            <div class="mf-text">+971554418701</div>
                        </li>
                        <li class="mf-contact-item">
                            <div class="mf-icon"><svg><use href="#icon-location"></use></svg></div>
                            <div class="mf-text">Corniche Building, Corniche Street,<br/>Abudhabi</div>
                        </li>
                        <li class="mf-contact-item">
                            <div class="mf-icon"><svg><use href="#icon-email"></use></svg></div>
                            <div class="mf-text">info@teamoak.co</div>
                        </li>
                    </ul>
                </div>
                <div class="mf-col">
                    <h4 data-i18n="global_navigate">Navigate</h4>
                    <ul>
                        <li><a data-i18n="global_home" href="index.html">Home</a></li>
                        <li><a data-i18n="global_about_us_2" href="about.html">About Us</a></li>
                        <li><a data-i18n="global_media" href="media.html">Media</a></li>
                        <li><a data-i18n="global_career" href="career.html">Career</a></li>
                        <li><a data-i18n="global_contact_us" href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                <div class="mf-col">
                    <h4 data-i18n="global_our_ventures">Our Ventures</h4>
                    <div class="ventures-grid">
                        <ul>
                            <li data-i18n="about_team_oak_tobacco_wholesale_trading"><a href="tobacco-trading.html">Team Oak Tobacco Wholesale Trading</a></li>
                            <li data-i18n="about_team_oak_food_stuff_trading"><a href="food-stuff-trading.html">Team Oak Food Stuff Trading Company</a></li>
                            <li data-i18n="about_kizhissery_jewellers"><a href="kizhisseri-jewellers.html">Kizhissery Jewellers</a></li>
                            <li data-i18n="about_team_oak_general_trading_company"><a href="general-trading.html">Team Oak General Trading Company</a></li>
                            <li data-i18n="about_makin_spare_parts_trading_company"><a href="makin-spare-parts-trading.html">Makin Spare parts Trading Company</a></li>
                            <li data-i18n="about_sugar_packing_unit"><a href="sugar-packing.html">Sugar packing Unit</a></li>
                        </ul>
                        <ul>
                            <li data-i18n="about_best_vibes_general_contracting_llc"><a href="best-vibes-contracting.html">Best Vibes General Contracting LLC</a></li>
                            <li data-i18n="about_bubbl"><a href="bubbl.html">Bubbl</a></li>
                            <li data-i18n="about_cafein"><a href="cafein.html">Cafein</a></li>
                            <li data-i18n="about_mamichi_apartments"><a href="mamichi-apartments.html">Mamichi Apartments</a></li>
                            <li data-i18n="about_oak_academy_of_design"><a href="oak-academy-of-design.html">Oak Academy of Design</a></li>
                            <li data-i18n="about_oak_architects_amp_interiors"><a href="oak-architects.html">Oak Architects &amp; Interiors</a></li>
                        </ul>
                        <ul>
                            <li data-i18n="about_pharma_fleet"><a href="pharma-fleet.html">Pharma Fleet</a></li>
                            <li data-i18n="about_team_oak_builders_amp_developers"><a href="team-oak-builders.html">Team Oak Builders &amp; Developers</a></li>
                            <li data-i18n="about_team_oak_logistics_services"><a href="team-oak-logistics.html">Team Oak Logistics Services</a></li>
                            <li data-i18n="about_team_oak_safety_amp_fire"><a href="team-oak-safety.html">Team Oak Safety &amp; Fire Fighting Equipment LLC</a></li>
                            <li data-i18n="about_team_oak_transport_amp_heavy"><a href="team-oak-transport.html">Team Oak Transport &amp; Heavy Equipment Rental LLC</a></li>
                            <li data-i18n="about_wymax_media"><a href="wymax-media.html">WYMAX MEDIA</a></li>
                        </ul>
                    </div>
                </div>
                <div class="mf-col follow-us-col">
                    <h4 data-i18n="global_follow_us">Follow Us</h4>
                    <ul>
                        <li data-i18n="about_facebook"><a href="https://www.facebook.com/share/1HXbqFMMr1/" target="_blank">Facebook</a></li>
                        <li data-i18n="about_instagram"><a href="https://www.instagram.com/_oak_architects?igsh=a3lnM3pucXB3djk2" target="_blank">Instagram</a></li>
                        <li data-i18n="about_linkedin"><a href="https://www.linkedin.com/company/team-oak/" target="_blank">LinkedIn</a></li>
                        <li data-i18n="about_youtube"><a href="https://youtube.com/@theoakteam8268?si=32MAruPZFb6WyC8a" target="_blank">YouTube</a></li>
                    </ul>
                </div>
            </div>
            <div class="mf-bottom">
                <div class="mf-copy">© Copyright Team Oak. All rights reserved. 2026</div>
                <div class="mf-legal">
                    <a data-i18n="global_privacy_policy" href="#">Privacy &amp; Policy</a>
                    <a data-i18n="global_terms_conditions" href="#">Terms &amp; Condition</a>
                </div>
            </div>
        </div>
    </footer>'''

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # We want to replace everything from <footer to </footer> or starting with svg icon definitions if present
    if '<svg style="display:none;">' in content and '</footer>' in content:
        start_idx = content.find('<svg style="display:none;">')
        end_idx = content.find('</footer>', start_idx) + len('</footer>')
        new_content = content[:start_idx] + footer_html + content[end_idx:]
    else:
        new_content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL | re.IGNORECASE)
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated footer in {f}')
