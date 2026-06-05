import os
import glob

def main():
    directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
    html_files = glob.glob(os.path.join(directory, "*.html"))
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content.replace("Info@teamoak.co", "info@teamoak.co")
        new_content = new_content.replace("contact@teamoak.com", "info@teamoak.co")
        
        if content != new_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(file_path)}")

if __name__ == "__main__":
    main()
