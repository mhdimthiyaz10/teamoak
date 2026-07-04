import glob

GT_CODE = """
<div id="google_translate_element" style="display:none;"></div>
<script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', autoDisplay: false}, 'google_translate_element');
}

function setLanguage(lang) {
    var selectField = document.querySelector(".goog-te-combo");
    if (selectField) {
        selectField.value = lang;
        selectField.dispatchEvent(new Event("change"));
    }
}
</script>
<script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
"""

def main():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'google_translate_element' not in content:
            # Insert before <script src="lang-switcher.js"></script> or </body>
            if '<script src="lang-switcher.js"></script>' in content:
                content = content.replace('<script src="lang-switcher.js"></script>', GT_CODE + '\\n    <script src="lang-switcher.js"></script>')
            else:
                content = content.replace('</body>', GT_CODE + '\\n</body>')
                
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Added Google Translate to {file}")

if __name__ == '__main__':
    main()
