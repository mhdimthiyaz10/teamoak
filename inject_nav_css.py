import os

css_to_inject = """
    <style>
        /* ═══════════════════════════
           MEGA MENU OVERRIDE
        ═══════════════════════════ */
        .nav-links li.has-arrow .dropdown {
            position: absolute !important;
            top: calc(100% + 10px) !important;
            left: 50% !important;
            transform: translateX(-50%) translateY(-10px) !important;
            background: #ffffff !important;
            border-radius: 12px !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08) !important;
            padding: 1.5rem !important;
            min-width: 220px !important;
            opacity: 0;
            pointer-events: none;
            transition: all 0.3s ease !important;
            border: none !important;
        }

        .nav-links li.has-arrow:hover .dropdown, 
        .nav-links li.has-arrow.open .dropdown {
            opacity: 1 !important;
            pointer-events: all !important;
            transform: translateX(-50%) translateY(0) !important;
        }

        .nav-links li.has-arrow .dropdown > li > a {
            display: flex !important;
            align-items: center !important;
            justify-content: space-between !important;
            padding: 1rem 1.5rem !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 0.95rem !important;
            font-weight: 700 !important;
            color: #111111 !important;
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            border-radius: 8px !important;
            margin: 0.3rem 0 !important;
            background: transparent !important;
        }

        /* Arrow for the left menu items */
        .nav-links li.has-arrow .dropdown > li > a::after {
            content: "\\203A";
            font-size: 1.4rem;
            font-weight: 300;
            margin-left: 2rem;
            color: #888;
        }

        .nav-links li.has-arrow .dropdown > li > a:hover,
        .nav-links li.has-arrow .dropdown > li.active > a,
        .nav-links li.has-arrow .dropdown > li:hover > a {
            background: transparent !important;
            color: #111111 !important;
        }

        /* Right Panel (Flyout) */
        .nav-links li.has-arrow .dropdown li.has-flyout .flyout {
            position: absolute !important;
            top: 0 !important;
            left: calc(100% + 10px) !important;
            background: #ffffff !important;
            border-radius: 12px !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08) !important;
            padding: 1.5rem 1rem !important;
            min-width: 380px !important;
            opacity: 0;
            pointer-events: none;
            transform: translateX(-10px) !important;
            transition: all 0.3s ease !important;
            border: none !important;
            display: block !important;
        }

        /* CSS trick to show first tab by default */
        .nav-links li.has-arrow .dropdown > li.has-flyout:first-child .flyout {
            opacity: 1 !important;
            pointer-events: all !important;
            transform: translateX(0) !important;
        }
        .nav-links li.has-arrow .dropdown:hover > li.has-flyout:first-child:not(:hover) .flyout {
            opacity: 0 !important;
            pointer-events: none !important;
            transform: translateX(-10px) !important;
        }
        .nav-links li.has-arrow .dropdown > li.has-flyout:hover .flyout,
        .nav-links li.has-arrow .dropdown > li.has-flyout.active .flyout {
            opacity: 1 !important;
            pointer-events: all !important;
            transform: translateX(0) !important;
            z-index: 10;
        }

        /* Flyout Links */
        .nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {
            padding: 1rem 1.2rem !important;
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            font-size: 0.95rem !important;
            font-weight: 600 !important;
            color: #444444 !important;
            text-transform: none !important;
            border-radius: 8px !important;
            margin: 0.2rem 0 !important;
            transition: all 0.2s ease !important;
            background: transparent !important;
            letter-spacing: 0 !important;
            display: block !important;
        }

        /* Hover state matching the image: Gold text, light grey background */
        .nav-links li.has-arrow .dropdown li.has-flyout .flyout li a:hover {
            color: #c59b27 !important;
            background: #f7f7f7 !important;
        }
        
        /* Fix for mobile screens */
        @media (max-width: 1024px) {
            .nav-links li.has-arrow .dropdown {
                display: none !important; /* Let mobile nav handle it if there is one */
            }
        }
    </style>
"""

files_to_update = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files_to_update:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid duplicate injection
    if "MEGA MENU OVERRIDE" in content:
        print(f"Skipping {filename}, already has override.")
        continue

    # Insert just before </head>
    if "</head>" in content:
        new_content = content.replace("</head>", css_to_inject + "\n</head>")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No </head> tag found in {filename}")
