import os
import re

dropdown_html = '''<li class="has-arrow"><a data-i18n="global_what_we_do" href="javascript:void(0);">What We Do</a>
                <ul class="dropdown">
                    <li class="has-flyout"><a data-i18n="global_trading" href="javascript:void(0);">Trading</a>
                        <ul class="flyout">
                            <li data-i18n="about_team_oak_tobacco_wholesale_trading"><a href="tobacco-trading.html">Team Oak Tobacco Wholesale Trading</a></li>
                            <li data-i18n="about_team_oak_food_stuff_trading"><a href="food-stuff-trading.html">Team Oak Food Stuff Trading Company</a></li>
                            <li data-i18n="about_kizhissery_jewellers"><a href="kizhisseri-jewellers.html">Kizhissery Jewellers</a></li>
                            <li data-i18n="about_team_oak_general_trading_company"><a href="general-trading.html">Team Oak General Trading Company</a></li>
                            <li data-i18n="about_makin_spare_parts_trading_company"><a href="makin-spare-parts-trading.html">Makin Spare parts Trading Company</a></li>
                        </ul>
                    </li>
                    <li class="has-flyout"><a data-i18n="global_services" href="javascript:void(0);">Services</a>
                        <ul class="flyout">
                            <li data-i18n="about_best_vibes_general_contracting_llc"><a href="best-vibes-contracting.html">Best Vibes General Contracting LLC</a></li>
                            <li data-i18n="about_bubbl"><a href="bubbl.html">Bubbl</a></li>
                            <li data-i18n="about_cafein"><a href="cafein.html">Cafein</a></li>
                            <li data-i18n="about_mamichi_apartments"><a href="mamichi-apartments.html">Mamichi Apartments</a></li>
                            <li data-i18n="about_oak_academy_of_design"><a href="oak-academy-of-design.html">Oak Academy of Design</a></li>
                            <li data-i18n="about_oak_architects_amp_interiors"><a href="oak-architects.html">Oak Architects &amp; Interiors</a></li>
                            <li data-i18n="about_pharma_fleet"><a href="pharma-fleet.html">Pharma Fleet</a></li>
                            <li data-i18n="about_team_oak_builders_amp_developers"><a href="team-oak-builders.html">Team Oak Builders &amp; Developers</a></li>
                            <li data-i18n="about_team_oak_logistics_services"><a href="team-oak-logistics.html">Team Oak Logistics Services</a></li>
                            <li data-i18n="about_team_oak_safety_amp_fire"><a href="team-oak-safety.html">Team Oak Safety &amp; Fire Fighting Equipment LLC</a></li>
                            <li data-i18n="about_team_oak_transport_amp_heavy"><a href="team-oak-transport.html">Team Oak Transport &amp; Heavy Equipment Rental LLC</a></li>
                            <li data-i18n="about_wymax_media"><a href="wymax-media.html">WYMAX MEDIA</a></li>
                        </ul>
                    </li>
                    <li class="has-flyout"><a data-i18n="global_industrial" href="javascript:void(0);">Industrial</a>
                        <ul class="flyout">
                            <li data-i18n="about_sugar_packing_unit"><a href="sugar-packing.html">Sugar packing Unit</a></li>
                        </ul>
                    </li>
                </ul>
            </li>'''

# For the mobile fix, we add a touch event listener at the end of the script block, or body.
script_injection = '''
<script>
document.addEventListener('DOMContentLoaded', function() {
    var arrows = document.querySelectorAll('.has-arrow > a, .has-flyout > a');
    arrows.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            this.parentElement.classList.toggle('open');
        });
    });
});
</script>
'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Regex to find the <li class="has-arrow"> block
        # It matches until the end of the outer <li>
        new_content = re.sub(r'<li class="has-arrow">\s*<a[^>]*>(?:What We Do|What we do)[\s\S]*?</li>', dropdown_html, content)

        # Inject script before </body> if not already there
        if 'arrows.forEach(function(btn)' not in new_content:
            new_content = new_content.replace('</body>', script_injection + '\n</body>')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
