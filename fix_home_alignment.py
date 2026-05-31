import os

filepath = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm\index.html"

fix_css = """
<!-- HOME ALIGNMENT FIX -->
<style>
@media (max-width: 768px) {
    /* Add proper breathing room to the entire About/WWD section */
    .about-wwd-unified {
        padding-left: 6% !important;
        padding-right: 6% !important;
        box-sizing: border-box !important;
        width: 100% !important;
        overflow: hidden !important;
    }
    
    /* Ensure the text is nicely aligned and readable */
    .scroll-reveal-text {
        text-align: left !important;
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }
    
    /* Ensure the What We Do cards don't break out of bounds */
    .wwd-grid {
        display: flex !important;
        flex-direction: column !important;
        gap: 1.5rem !important;
    }
    
    .wwd-card {
        width: 100% !important;
        box-sizing: border-box !important;
        margin: 0 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
    }
}
</style>
<!-- END HOME ALIGNMENT FIX -->
"""

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

if '<!-- HOME ALIGNMENT FIX -->' not in content:
    content = content.replace('</head>', fix_css + '\n</head>')
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed alignments in index.html")
