import glob

html_files = glob.glob('*.html')

# Extract footer from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

start_marker = '<svg style="display:none;">'
end_marker = '</footer>'

start_idx = index_content.find(start_marker)
end_idx = index_content.find(end_marker, start_idx) + len(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find footer in index.html")
    exit(1)

footer_content = index_content[start_idx:end_idx]

for file in html_files:
    if file == 'index.html':
        continue
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    f_start_idx = content.find(start_marker)
    f_end_idx = content.find(end_marker, f_start_idx) + len(end_marker)
    
    if f_start_idx != -1 and f_end_idx != -1:
        new_content = content[:f_start_idx] + footer_content + content[f_end_idx:]
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {file}")
    else:
        print(f"Could not find footer markers in {file}, skipping.")

print("Finished updating all footers.")
