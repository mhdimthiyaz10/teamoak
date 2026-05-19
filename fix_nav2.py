import os
import re

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

        # We look for <li class="has-arrow"> up to the <li> that contains Media
        # This prevents eating up the rest of the file
        pattern = r'<li class="has-arrow">\s*<a[^>]*>(?:What We Do|What we do)[\s\S]*?</li>\s*(?=<li>\s*<a[^>]*>Media</a>\s*</li>)'
        
        # BUT for contact.html and career.html, my broken script left dangling </ul></li> which might ruin it.
        # Let's fix those manually or let the regex fix it if they still match Media.
        new_content = re.sub(pattern, dropdown_html + '\n            ', content)

        if 'arrows.forEach(function(btn)' not in new_content:
            new_content = new_content.replace('</body>', script_injection + '\n</body>')

        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {file}")
