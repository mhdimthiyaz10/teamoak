import os
from bs4 import BeautifulSoup

dropdown_html = '''<li class="has-arrow"><a href="javascript:void(0);">What We Do</a>
    <ul class="dropdown">
        <li class="has-flyout"><a href="javascript:void(0);">Trading</a>
            <ul class="flyout">
                <li><a href="tobacco-trading.html">Team Oak Tobacco Wholesale Trading</a></li>
                <li><a href="food-stuff-trading.html">Team Oak Food Stuff Trading Company</a></li>
                <li><a href="kizhisseri-jewellers.html">Kizhissery Jewellers</a></li>
                <li><a href="general-trading.html">Team Oak General Trading Company</a></li>
            </ul>
        </li>
        <li class="has-flyout"><a href="javascript:void(0);">Services</a>
            <ul class="flyout">
                <li><a href="best-vibes-contracting.html">Best Vibes General Contracting LLC</a></li>
                <li><a href="team-oak-hotels.html">Team Oak Hotels &amp; Apartments</a></li>
                <li><a href="team-oak-camps.html">Team Oak Resort Camps &amp; Trails</a></li>
                <li><a href="mamichi-apartments.html">Mamichi Apartments</a></li>
                <li><a href="oak-architects.html">Oak Architects &amp; Interiors</a></li>
                <li><a href="bubbl.html">Bubbl</a></li>
                <li><a href="team-oak-transport.html">Team Oak Transport &amp; Heavy Equipment Rental LLC</a></li>
                <li><a href="team-oak-safety.html">Team Oak Safety &amp; Fire Fighting Equipment LLC</a></li>
                <li><a href="cafein.html">Cafein</a></li>
                <li><a href="pharma-fleet.html">Pharma Fleet</a></li>
            </ul>
        </li>
        <li class="has-flyout"><a href="javascript:void(0);">Industrial</a>
            <ul class="flyout">
                <li><a href="sugar-packing.html">Sugar packing Unit</a></li>
            </ul>
        </li>
    </ul>
</li>'''

for file in os.listdir('.'):
    if file.endswith('.html'):
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        # Find the <li class="has-arrow"> that contains "What We Do"
        has_arrow_lis = soup.find_all('li', class_='has-arrow')
        for li in has_arrow_lis:
            a_tag = li.find('a')
            if a_tag and 'what we do' in a_tag.text.lower():
                # We found it. Let's replace this entire tag with our new parsed tag
                new_tag = BeautifulSoup(dropdown_html, 'html.parser').li
                li.replace_with(new_tag)
                break
                
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Fixed {file}")
