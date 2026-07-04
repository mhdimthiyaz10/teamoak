import glob

def main():
    html_files = glob.glob('*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        
        # Replace the literal \n that was accidentally injected
        if '\\n    <script src="lang-switcher.js"></script>' in content:
            content = content.replace('\\n    <script src="lang-switcher.js"></script>', '\n    <script src="lang-switcher.js"></script>')
            modified = True
            
        if modified:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed literal newline in {file}")

if __name__ == '__main__':
    main()
