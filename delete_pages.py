import os
import re

def main():
    files_to_delete = ['team-oak-hotels.html', 'team-oak-camps.html']
    dir_path = '.'

    # Delete the files
    for f in files_to_delete:
        filepath = os.path.join(dir_path, f)
        if os.path.exists(filepath):
            try:
                os.remove(filepath)
                print(f"Deleted {f}")
            except Exception as e:
                print(f"Failed to delete {f}: {e}")

    # Update remaining html files to remove the links
    for filename in os.listdir(dir_path):
        if filename.endswith('.html'):
            filepath = os.path.join(dir_path, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Regex to match the entire <li> containing the link, including trailing whitespace/newlines
            pattern_hotels = r'<li[^>]*>\s*<a[^>]*href="team-oak-hotels\.html"[^>]*>.*?</a>\s*</li>\s*'
            pattern_camps = r'<li[^>]*>\s*<a[^>]*href="team-oak-camps\.html"[^>]*>.*?</a>\s*</li>\s*'
            
            new_content = re.sub(pattern_hotels, '', content, flags=re.DOTALL)
            new_content = re.sub(pattern_camps, '', new_content, flags=re.DOTALL)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")

if __name__ == '__main__':
    main()
