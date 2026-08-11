import os
import glob
import re

def update_scrollbars():
    directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
    html_files = glob.glob(os.path.join(directory, "*.html"))
    
    # This pattern matches any previous custom scrollbar blocks we added
    pattern = re.compile(
        r"(\.nav-links li\.has-arrow \.dropdown li\.has-flyout \.flyout(?:::-webkit-scrollbar(?:-[a-z]+)?|)\s*\{[^}]*\}\s*)+",
        re.DOTALL
    )

    new_css = """.nav-links li.has-arrow .dropdown li.has-flyout .flyout {
            scrollbar-width: auto !important;
            scrollbar-color: #000000 #f4f4f4 !important;
        }
        .nav-links li.has-arrow .dropdown li.has-flyout .flyout::-webkit-scrollbar {
            width: 14px !important;
        }
        .nav-links li.has-arrow .dropdown li.has-flyout .flyout::-webkit-scrollbar-track {
            background: #f4f4f4 !important;
            border-radius: 8px !important;
            margin: 5px 0 !important;
        }
        .nav-links li.has-arrow .dropdown li.has-flyout .flyout::-webkit-scrollbar-thumb {
            background: #000000 !important;
            border-radius: 8px !important;
            border: 2px solid #f4f4f4 !important;
        }
        .nav-links li.has-arrow .dropdown li.has-flyout .flyout::-webkit-scrollbar-thumb:hover {
            background: #333333 !important;
        }
        """

    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if "flyout::-webkit-scrollbar" in content:
            new_content = pattern.sub(new_css, content)
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {os.path.basename(file_path)}")

if __name__ == "__main__":
    update_scrollbars()
