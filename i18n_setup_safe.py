import os
import json
import re
import sys
import time
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Print helper to flush immediately
def print_flush(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()

DESKTOP_SWITCHER_HTML = """
<div class="premium-lang-switcher desktop-switcher">
    <button class="pls-btn" aria-label="Select Language" aria-expanded="false">
        <svg class="pls-globe" viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
        <span class="pls-current">EN</span>
        <svg class="pls-arrow" viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
    </button>
    <div class="pls-dropdown">
        <button class="pls-option active" data-lang="en">
            <span class="pls-code">EN</span>
            <span class="pls-name">English</span>
        </button>
        <button class="pls-option" data-lang="ar">
            <span class="pls-code">ع</span>
            <span class="pls-name">العربية</span>
        </button>
    </div>
</div>
"""

MOBILE_SWITCHER_HTML = """
<li class="mobile-switcher-li">
    <div class="premium-lang-switcher mobile-switcher">
        <button class="pls-btn" aria-label="Select Language" aria-expanded="false">
            <svg class="pls-globe" viewBox="0 0 24 24" width="16" height="16" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
            <span class="pls-current">EN</span>
            <svg class="pls-arrow" viewBox="0 0 24 24" width="14" height="14" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
        </button>
        <div class="pls-dropdown">
            <button class="pls-option active" data-lang="en">
                <span class="pls-code">EN</span>
                <span class="pls-name">English</span>
            </button>
            <button class="pls-option" data-lang="ar">
                <span class="pls-code">ع</span>
                <span class="pls-name">العربية</span>
            </button>
        </div>
    </div>
</li>
"""

PREDEFINED_KEYS = {
    "home": "global_home",
    "about us": "global_about_us",
    "what we do": "global_what_we_do",
    "trading": "global_trading",
    "services": "global_services",
    "industrial": "global_industrial",
    "media": "global_media",
    "career": "global_career",
    "contact us": "global_contact_us",
    "contact": "global_contact",
    "navigate": "global_navigate",
    "our ventures": "global_our_ventures",
    "follow us": "global_follow_us",
    "privacy & policy": "global_privacy_policy",
    "terms & condition": "global_terms_conditions"
}

keys_used = {}

def clean_key(text):
    text_lower = text.lower().strip()
    text_clean = re.sub(r'<[^>]+>', '', text_lower).strip()
    if text_clean in PREDEFINED_KEYS:
        return PREDEFINED_KEYS[text_clean]
    
    clean = re.sub(r'[^\w\s]', '', text_clean)
    words = clean.split()
    if not words:
        return "key_" + str(abs(hash(text)) % 1000000)
    
    base_key = "_".join(words[:5])
    return base_key

def get_unique_key(text, page_prefix):
    base_key = clean_key(text)
    if not base_key.startswith("global_"):
        base_key = f"{page_prefix}_{base_key}"
        
    if base_key not in keys_used:
        keys_used[base_key] = text
        return base_key
    else:
        if keys_used[base_key] == text:
            return base_key
        counter = 2
        new_key = f"{base_key}_{counter}"
        while new_key in keys_used and keys_used[new_key] != text:
            counter += 1
            new_key = f"{base_key}_{counter}"
        keys_used[new_key] = text
        return new_key

def extract_and_annotate(element, string_to_key, page_prefix):
    if element.name in ['script', 'style', 'noscript']:
        return
        
    is_translatable = False
    
    if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'button', 'span', 'li', 'label', 'strong', 'em']:
        has_block_child = any(
            c.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'div', 'section', 'ul', 'ol', 'li', 'footer', 'header', 'nav']
            for c in element.find_all()
        )
        if not has_block_child:
            inner_html = "".join([str(c) for c in element.contents]).strip()
            clean_html = re.sub(r'\s+', ' ', inner_html)
            plain_text = re.sub(r'<[^>]+>', '', clean_html).strip()
            
            if plain_text and len(plain_text) > 1 and not re.match(r'^[0-9\s\+\-\(\):,\.\&/]+$', plain_text):
                is_translatable = True
                if clean_html not in string_to_key:
                    string_to_key[clean_html] = get_unique_key(clean_html, page_prefix)
                element['data-i18n'] = string_to_key[clean_html]
                
    if element.name in ['input', 'textarea']:
        placeholder = element.get('placeholder')
        if placeholder:
            text = placeholder.strip()
            if text:
                if text not in string_to_key:
                    string_to_key[text] = get_unique_key(text, page_prefix)
                element['data-i18n-placeholder'] = string_to_key[text]
                
    if element.name == 'img':
        alt = element.get('alt')
        if alt:
            text = alt.strip()
            if text:
                if text not in string_to_key:
                    string_to_key[text] = get_unique_key(text, page_prefix)
                element['data-i18n-alt'] = string_to_key[text]
                
    if is_translatable:
        return
        
    for child in list(element.children):
        if child.name:
            extract_and_annotate(child, string_to_key, page_prefix)

def translate_batch_safe(strings):
    translator = GoogleTranslator(source='en', target='ar')
    translated = []
    chunk_size = 20  # smaller chunk size
    
    for i in range(0, len(strings), chunk_size):
        chunk = strings[i:i+chunk_size]
        print_flush(f"Translating batch {i//chunk_size + 1} of {(len(strings)-1)//chunk_size + 1}...")
        
        # Try chunk translation
        try:
            results = translator.translate_batch(chunk)
            translated.extend(results)
            time.sleep(1.0) # sleep 1 second between batches to avoid rate limit
        except Exception as e:
            print_flush(f"Error in batch translation: {e}. Falling back to single translation with delay.")
            for s in chunk:
                try:
                    res = translator.translate(s)
                    translated.append(res)
                    time.sleep(0.5)
                except Exception as ex:
                    print_flush(f"Failed to translate: '{s}'. Error: {ex}")
                    translated.append(s) # Fallback to english
                    time.sleep(1.0)
    return translated

def cleanup_arabic_html(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r'<\s*strong\s*>', '<strong>', text)
    text = re.sub(r'<\s*/\s*strong\s*>', '</strong>', text)
    text = re.sub(r'<\s*em\s*>', '<em>', text)
    text = re.sub(r'<\s*/\s*em\s*>', '</em>', text)
    text = re.sub(r'<\s*br\s*/?\s*>', '<br>', text)
    text = re.sub(r'<\s*span\s*>', '<span>', text)
    text = re.sub(r'<\s*/\s*span\s*>', '</span>', text)
    return text

def main():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    print_flush(f"Found {len(html_files)} HTML files to process.")
    
    string_to_key = {}
    
    # First pass: Extract and annotate
    for file in html_files:
        print_flush(f"Annotating {file}...")
        page_prefix = file.replace('.html', '').replace('-', '_')
        
        with open(file, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        if soup.title and soup.title.string:
            title_text = soup.title.string.strip()
            if title_text:
                if title_text not in string_to_key:
                    string_to_key[title_text] = get_unique_key(title_text, page_prefix)
                soup.title['data-i18n'] = string_to_key[title_text]
                
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            desc_text = meta_desc.get('content').strip()
            if desc_text:
                if desc_text not in string_to_key:
                    string_to_key[desc_text] = get_unique_key(desc_text, page_prefix)
                meta_desc['data-i18n'] = string_to_key[desc_text]
                
        if soup.body:
            extract_and_annotate(soup.body, string_to_key, page_prefix)
            
        nav_actions = soup.find(class_='nav-actions')
        if nav_actions:
            if not nav_actions.find(class_='desktop-switcher'):
                nav_actions.append(BeautifulSoup(DESKTOP_SWITCHER_HTML, 'html.parser'))
                
        nav_links = soup.find('ul', class_=re.compile(r'(hero-)?nav-links'))
        if nav_links:
            if not nav_links.find(class_='mobile-switcher-li'):
                nav_links.append(BeautifulSoup(MOBILE_SWITCHER_HTML, 'html.parser'))
                
        if soup.body:
            if not soup.find('script', src='translator.js'):
                script_tag = soup.new_tag('script', src='translator.js', defer=True)
                soup.body.append(script_tag)
                
        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
    print_flush(f"HTML files annotated. Total unique strings: {len(string_to_key)}")
    
    # Translate strings
    english_strings = list(string_to_key.keys())
    print_flush("Starting translation to Arabic...")
    arabic_strings = translate_batch_safe(english_strings)
    
    en_translations = {}
    ar_translations = {}
    
    for en_str, ar_str in zip(english_strings, arabic_strings):
        key = string_to_key[en_str]
        en_translations[key] = en_str
        ar_translations[key] = cleanup_arabic_html(ar_str)
        
    overrides = {
        "global_home": ("Home", "الرئيسية"),
        "global_about_us": ("About Us", "من نحن"),
        "global_what_we_do": ("What We Do", "ماذا نفعل"),
        "global_trading": ("Trading", "التجارة"),
        "global_services": ("Services", "الخدمات"),
        "global_industrial": ("Industrial", "الصناعة"),
        "global_media": ("Media", "الإعلام"),
        "global_career": ("Career", "الوظائف"),
        "global_contact_us": ("Contact Us", "اتصل بنا"),
        "global_contact": ("Contact", "اتصل بنا"),
        "global_navigate": ("Navigate", "تصفح الموقع"),
        "global_our_ventures": ("Our Ventures", "مشاريعنا"),
        "global_follow_us": ("Follow Us", "تابعنا"),
        "global_privacy_policy": ("Privacy & Policy", "سياسة الخصوصية"),
        "global_terms_conditions": ("Terms & Condition", "الشروط والأحكام")
    }
    
    for key, (en_val, ar_val) in overrides.items():
        if key in en_translations:
            en_translations[key] = en_val
            ar_translations[key] = ar_val
            
    with open('en.json', 'w', encoding='utf-8') as f:
        json.dump(en_translations, f, ensure_ascii=False, indent=4)
        
    with open('ar.json', 'w', encoding='utf-8') as f:
        json.dump(ar_translations, f, ensure_ascii=False, indent=4)
        
    print_flush("en.json and ar.json successfully generated.")

if __name__ == '__main__':
    main()
