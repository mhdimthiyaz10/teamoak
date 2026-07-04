import glob

html_files = glob.glob('*.html')
makin_href = 'makin-spare-parts-trading.html'

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    in_ventures_grid = False
    ventures_ul_count = 0
    makin_line = ''
    
    # First pass: find and remove makin_line from the footer
    for line in lines:
        if 'class="ventures-grid"' in line:
            in_ventures_grid = True
            
        if in_ventures_grid:
            if '<ul' in line:
                ventures_ul_count += 1
            if '</div' in line and ventures_ul_count == 3: # heuristic
                in_ventures_grid = False
                
            if makin_href in line:
                makin_line = line
                continue # skip adding it to new_lines (remove it)
                
        new_lines.append(line)
        
    # Second pass: insert it at the end of the second ul
    final_lines = []
    in_ventures_grid = False
    ventures_ul_count = 0
    
    for line in new_lines:
        if 'class="ventures-grid"' in line:
            in_ventures_grid = True
            
        if in_ventures_grid:
            if '<ul' in line:
                ventures_ul_count += 1
                
            # If we hit the end of the second ul, insert our line before it
            if '</ul>' in line and ventures_ul_count == 2:
                if makin_line:
                    final_lines.append(makin_line)
                in_ventures_grid = False # Stop inserting
                
        final_lines.append(line)
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(''.join(final_lines))
        
print("Successfully moved Makeen SpareParts Trading to the second column.")
