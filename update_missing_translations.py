import json
import re
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import time

def main():
    files = ['media.html', 'career.html']
    with open('en.json', 'r', encoding='utf-8') as f:
        en_json = json.load(f)
    with open('ar.json', 'r', encoding='utf-8') as f:
        ar_json = json.load(f)

    translator = GoogleTranslator(source='en', target='ar')
    added = 0

    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')

        # Find all elements with data-i18n
        elements = soup.find_all(attrs={"data-i18n": True})
        
        # Also meta tags and title
        if soup.title and soup.title.get('data-i18n'):
            elements.append(soup.title)
        
        for el in elements:
            key = el.get('data-i18n')
            if not key:
                continue

            if key not in en_json or key not in ar_json:
                # Extract english text
                if el.name == 'meta':
                    text = el.get('content', '')
                else:
                    inner_html = "".join([str(c) for c in el.contents]).strip()
                    clean_html = re.sub(r'\s+', ' ', inner_html)
                    text = re.sub(r'<[^>]+>', '', clean_html).strip()

                if text:
                    print(f"Translating {key}: {text}")
                    en_json[key] = clean_html
                    try:
                        ar_text = translator.translate(text)
                        
                        # Fix up HTML tags if they were in clean_html
                        if "<em>" in clean_html:
                            ar_text = f"<em>{ar_text}</em>"
                        if "<br/>" in clean_html or "<br>" in clean_html:
                            ar_text = ar_text.replace('\n', '<br>')
                            
                        ar_json[key] = ar_text
                        time.sleep(0.5)
                        added += 1
                    except Exception as e:
                        print(f"Failed to translate {text}: {e}")
                        ar_json[key] = text

    if added > 0:
        with open('en.json', 'w', encoding='utf-8') as f:
            json.dump(en_json, f, ensure_ascii=False, indent=4)
        with open('ar.json', 'w', encoding='utf-8') as f:
            json.dump(ar_json, f, ensure_ascii=False, indent=4)
        print(f"Added {added} missing translations.")
    else:
        print("No missing translations found.")

if __name__ == '__main__':
    main()
