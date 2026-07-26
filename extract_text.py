import os
import json
import re
from bs4 import BeautifulSoup

def extract_strings():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    all_texts = {}
    
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
        
        # Extract title
        if soup.title and soup.title.string:
            text = soup.title.string.strip()
            if text:
                all_texts[text] = all_texts.get(text, []) + [f"{file}:title"]
                
        # Extract meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            text = meta_desc.get('content').strip()
            if text:
                all_texts[text] = all_texts.get(text, []) + [f"{file}:meta_desc"]
        
        # Find all text elements
        for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'button', 'label', 'li', 'strong', 'em']):
            # Skip if it is inside script or style
            if tag.parent.name in ['script', 'style']:
                continue
            
            # Check direct text to avoid nested duplicates
            for content in tag.contents:
                if isinstance(content, str):
                    text = content.strip()
                    # Clean up multiple whitespaces
                    text = re.sub(r'\s+', ' ', text)
                    if text and len(text) > 1:
                        # Skip if it's purely numbers or special chars
                        if re.match(r'^[0-9\s\+\-\(\):,\.\&/]+$', text):
                            continue
                        all_texts[text] = all_texts.get(text, []) + [f"{file}:{tag.name}"]
                        
        # Extract placeholders
        for tag in soup.find_all(['input', 'textarea']):
            placeholder = tag.get('placeholder')
            if placeholder:
                text = placeholder.strip()
                if text:
                    all_texts[text] = all_texts.get(text, []) + [f"{file}:placeholder"]
                    
        # Extract image alts
        for tag in soup.find_all('img'):
            alt = tag.get('alt')
            if alt:
                text = alt.strip()
                if text:
                    all_texts[text] = all_texts.get(text, []) + [f"{file}:alt"]
                    
    # Save the extracted texts
    with open('extracted_texts.json', 'w', encoding='utf-8') as f:
        json.dump(all_texts, f, ensure_ascii=False, indent=4)
        
    print(f"Extracted {len(all_texts)} unique strings.")

if __name__ == '__main__':
    extract_strings()
