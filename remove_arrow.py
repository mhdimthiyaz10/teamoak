import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

css_to_add = """
    <style>
        /* Hide main nav arrow */
        .nav-links li.has-arrow > a::after {
            display: none !important;
            content: none !important;
        }
    </style>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '/* Hide main nav arrow */' not in content:
        # insert before </head>
        content = content.replace('</head>', css_to_add + '</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
