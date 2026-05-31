import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

css_to_add = """
    <style>
        /* Fix Nav Alignment for Tablet/Mobile */
        .nav-links a {
            white-space: nowrap !important;
        }
        @media (max-width: 1150px) {
            .nav-links {
                gap: 1.2rem !important;
            }
            .nav-links a {
                font-size: 0.65rem !important;
                letter-spacing: 1px !important;
            }
            .nav-btn {
                padding: 0.5rem 1.2rem !important;
                font-size: 0.65rem !important;
                white-space: nowrap !important;
            }
        }
    </style>
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '/* Fix Nav Alignment for Tablet/Mobile */' not in content:
        # insert before </head>
        content = content.replace('</head>', css_to_add + '</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {os.path.basename(filepath)}")
