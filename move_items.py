import glob
import os

html_files = glob.glob('*.html')
camps_str = '<li><a href="team-oak-camps.html">Team Oak Resort Camps &amp; Trails</a></li>'
makin_str = '<li><a href="makin-spare-parts-trading.html">Makeen SpareParts Trading</a></li>'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to remove camps_str and makin_str from wherever they are, 
    # and append them to the first <ul> inside <div class="ventures-grid">
    
    if camps_str in content and makin_str in content:
        # Remove them
        # Note: the lines might have leading spaces, so replacing the string itself works, but leaves empty lines.
        # Let's replace the string and strip empty lines later, or just replace the string.
        # Actually, replacing the exact string might leave whitespaces.
        
        # Split into lines
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if 'team-oak-camps.html' not in line and 'makin-spare-parts-trading.html' not in line:
                new_lines.append(line)
                
        content = '\n'.join(new_lines)
        
        # Now find the first </ul> after 'ventures-grid'
        idx = content.find('class="ventures-grid"')
        if idx != -1:
            ul_end_idx = content.find('</ul>', idx)
            if ul_end_idx != -1:
                # Insert them just before </ul>
                insert_str = '                            ' + camps_str + '\n                            ' + makin_str + '\n                        '
                content = content[:ul_end_idx] + insert_str + content[ul_end_idx:]
                
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print('Done moving camps and makin to the first column')
