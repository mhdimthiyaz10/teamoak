import os
import re

sorted_services_flyout = '''<li class="has-flyout"><a data-i18n="global_services" href="javascript:void(0);">Services</a>
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
</li>'''

sorted_nav_dropdown = f'''<li class="has-arrow"><a data-i18n="global_what_we_do" href="javascript:void(0);">What We Do</a>
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
{sorted_services_flyout}
<li class="has-flyout"><a data-i18n="global_industrial" href="javascript:void(0);">Industrial</a>
<ul class="flyout">
<li data-i18n="about_sugar_packing_unit"><a href="sugar-packing.html">Sugar packing Unit</a></li>
</ul>
</li>
</ul>
</li>'''

sorted_footer_ventures = '''<div class="mf-col">
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
</div>'''

def process_files():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    # Pattern to match the Services flyout in nav
    services_flyout_pattern = re.compile(
        r'<li class="has-flyout">\s*<a[^>]*>(?:Services|الخدمات)</a>\s*<ul class="flyout">[\s\S]*?</ul>\s*</li>',
        re.IGNORECASE
    )
    
    # Pattern to match the whole What We Do dropdown in nav
    what_we_do_pattern = re.compile(
        r'<li class="has-arrow">\s*<a[^>]*>(?:What We Do|What we do)</a>\s*<ul class="dropdown">[\s\S]*?</ul>\s*</li>',
        re.IGNORECASE
    )
    
    # Pattern to match the ventures grid in footer
    ventures_pattern = re.compile(
        r'<div class="mf-col">\s*<h4[^>]*>(?:Our Ventures|Services|مشاريعنا|الخدمات)</h4>\s*<div class="ventures-grid">[\s\S]*?</div>\s*</div>',
        re.IGNORECASE
    )
    
    updated_files = []
    for filename in html_files:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        
        # 1. Update Services flyout or What We Do dropdown
        if services_flyout_pattern.search(content):
            content = services_flyout_pattern.sub(sorted_services_flyout, content, count=1)
        elif what_we_do_pattern.search(content):
            content = what_we_do_pattern.sub(sorted_nav_dropdown, content, count=1)
            
        # 2. Update Footer Ventures
        if ventures_pattern.search(content):
            content = ventures_pattern.sub(sorted_footer_ventures, content, count=1)
            
        if content != orig:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            updated_files.append(filename)
            
    print(f"Updated {len(updated_files)} HTML files:")
    for uf in updated_files:
        print(f" - {uf}")

if __name__ == '__main__':
    process_files()
