import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'\.hero-nav-logo img\s*\{\s*height: 80px;\s*width: auto;\s*object-fit: contain;\s*display: block;\s*\}',
    '.hero-nav-logo img {\n    height: 80px;\n    width: auto;\n    object-fit: contain;\n    display: block;\n    filter: brightness(0) invert(1);\n}',
    content
)

content = re.sub(
    r'color: #000000;\s*text-shadow: 0 0 8px rgba\(255, 255, 255, 0\.9\), 0 0 15px rgba\(255, 255, 255, 0\.6\);',
    'color: #ffffff;\n    text-shadow: 0 0 8px rgba(0, 0, 0, 0.9), 0 0 15px rgba(0, 0, 0, 0.6);',
    content
)

content = re.sub(
    r'background: #000000;\s*transition: width 0\.3s cubic-bezier\(0\.4, 0, 0\.2, 1\);\s*box-shadow: 0 0 5px rgba\(255,255,255,0\.8\);',
    'background: #ffffff;\n    transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);\n    box-shadow: 0 0 5px rgba(0,0,0,0.8);',
    content
)

content = re.sub(
    r'color: #000000;\s*text-shadow: 0 0 8px rgba\(255, 255, 255, 0\.9\);\s*text-decoration: none;\s*border: 2px solid #000000;',
    'color: #ffffff;\n    text-shadow: 0 0 8px rgba(0, 0, 0, 0.9);\n    text-decoration: none;\n    border: 2px solid #ffffff;',
    content
)

content = re.sub(
    r'\.hero-nav-cta:hover\s*\{\s*background: #000000;\s*color: #ffffff;\s*border-color: #000000;\s*text-shadow: none;\s*\}',
    '.hero-nav-cta:hover {\n    background: #ffffff;\n    color: #000000;\n    border-color: #ffffff;\n    text-shadow: none;\n}',
    content
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated style.css successfully.")
