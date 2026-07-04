import glob
import os

html_files = glob.glob('*.html')
camps_href = 'team-oak-camps.html'
makin_href = 'makin-spare-parts-trading.html'
hotels_href = 'team-oak-hotels.html'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split lines
    lines = content.split('\n')
    
    # We will process line by line to remove team-oak-hotels globally
    # and to extract the footer instances of camps and makin, then insert them.
    
    new_lines = []
    
    in_ventures_grid = False
    ventures_ul_count = 0
    
    camps_line = ''
    makin_line = ''
    
    # First pass: find the exact lines for camps and makin in the footer, 
    # and remove hotels globally.
    for line in lines:
        if hotels_href in line:
            continue # drop hotels globally
            
        if 'class="ventures-grid"' in line:
            in_ventures_grid = True
            
        if in_ventures_grid:
            if '<ul' in line:
                ventures_ul_count += 1
            if '</div' in line and ventures_ul_count == 3: # rough heuristic to end
                in_ventures_grid = False
                
            if camps_href in line and ventures_ul_count > 1:
                camps_line = line
                continue # remove from current position
            if makin_href in line and ventures_ul_count > 1:
                makin_line = line
                continue # remove from current position
                
        new_lines.append(line)
        
    # Second pass: insert camps_line and makin_line into the first ul of ventures-grid
    final_lines = []
    in_ventures_grid = False
    ventures_ul_count = 0
    
    for line in new_lines:
        if 'class="ventures-grid"' in line:
            in_ventures_grid = True
            
        if in_ventures_grid:
            if '<ul' in line:
                ventures_ul_count += 1
                
            # If we hit the end of the first ul, insert our lines before it
            if '</ul>' in line and ventures_ul_count == 1:
                if camps_line:
                    final_lines.append(camps_line)
                if makin_line:
                    final_lines.append(makin_line)
                in_ventures_grid = False # Stop inserting
                
        final_lines.append(line)

    with open(file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(final_lines))

if os.path.exists('team-oak-hotels.html'):
    os.remove('team-oak-hotels.html')
    
print("Successfully updated footer and removed hotels page.")
