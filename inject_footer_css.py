import os
import re

css_to_inject = """
        /* ═══════════════════════════
           MINIMAL STANDARD FOOTER (WHITE THEME)
        ═══════════════════════════ */
        .minimal-footer {
            background-color: #ffffff;
            color: #111111;
            font-family: 'Plus Jakarta Sans', sans-serif;
            padding: 5rem 5% 2rem;
            border-top: 1px solid rgba(0,0,0,0.08);
            position: relative;
            z-index: 10;
        }
        .mf-container { max-width: 1300px; margin: 0 auto; }
        .mf-columns { display: grid; grid-template-columns: 2fr 1.5fr 1.5fr 1.5fr 1.5fr; gap: 3rem; padding-bottom: 4rem; }
        .mf-col h4 { font-family: 'Outfit', sans-serif; font-size: 1.15rem; font-weight: 700; color: #111111; margin-bottom: 2rem; letter-spacing: -0.2px; }
        .mf-col ul { list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 1.2rem; }
        .mf-col ul li a, .mf-text { font-size: 0.95rem; color: #555555; text-decoration: none; transition: color 0.3s; line-height: 1.5; }
        .mf-col ul li a:hover { color: #111111; }
        .mf-contact ul { gap: 1.5rem; }
        .mf-contact-item { display: flex; align-items: flex-start; gap: 1rem; }
        .mf-icon { width: 32px; height: 32px; border-radius: 50%; background-color: transparent; color: #c59b27; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 0 0 1px rgba(0,0,0,0.08); transition: all 0.3s ease; }
        .mf-icon svg { width: 16px; height: 16px; fill: currentColor; }
        .mf-text { padding-top: 5px; }
        .mf-bottom { display: flex; justify-content: space-between; align-items: center; padding-top: 2rem; border-top: 1px solid rgba(0,0,0,0.08); font-size: 0.9rem; color: #888888; }
        .mf-legal { display: flex; gap: 2rem; }
        .mf-legal a { color: #888888; text-decoration: none; transition: color 0.3s; }
        .mf-legal a:hover { color: #111111; }

        @media (max-width: 1024px) {
            .mf-columns { grid-template-columns: 1fr 1fr 1fr; gap: 3rem 2rem; }
            .mf-contact { grid-column: 1 / -1; }
        }
        @media (max-width: 640px) {
            .mf-columns { grid-template-columns: 1fr; }
            .mf-bottom { flex-direction: column; gap: 1.5rem; text-align: center; }
        }
"""

files_to_update = [
    "tobacco-trading.html",
    "food-stuff-trading.html",
    "kizhisseri-jewellers.html",
    "general-trading.html",
    "best-vibes-contracting.html",
    "team-oak-hotels.html",
    "team-oak-camps.html",
    "mamichi-apartments.html",
    "oak-architects.html",
    "bubbl.html",
    "team-oak-transport.html",
    "team-oak-safety.html",
    "cafein.html",
    "pharma-fleet.html",
    "sugar-packing.html"
]

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove old minimal-footer CSS if it exists
    content = re.sub(r'/\* ═══════════════════════════\s*MINIMAL STANDARD FOOTER.*\s*═══════════════════════════ \*/.*?@media \(max-width: 640px\) \{.*?\n        \}', '', content, flags=re.DOTALL)
    
    # Also just in case the previous script or format was different, try to strip .minimal-footer { ... } blocks up to the media query
    # But it's safer to just insert before </style> since duplicates won't break anything (the latter overrides).
    
    if "</style>" in content:
        # Check if we already injected it
        if "MINIMAL STANDARD FOOTER (WHITE THEME)" not in content:
            new_content = content.replace("</style>", css_to_inject + "\n    </style>")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
        else:
            print(f"Already updated {filename}")
    else:
        print(f"No </style> tag found in {filename}")
