import os
import re

def main():
    root = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
    files = [os.path.join(root, f) for f in os.listdir(root) if f.endswith(".html")]
    
    # We want to match these three lines:
    # if (page.indexOf('services-ngs-') === 0 && href === 'services-ngs.html') a.classList.add('is-active');
    # if (page.indexOf('services-dd-') === 0 && href === 'services-drug-discovery.html') a.classList.add('is-active');
    # if (page.indexOf('case-study-') === 0 && href === 'case-studies.html') a.classList.add('is-active');
    
    pattern_ngs = re.compile(r"if\s*\(\s*page\.indexOf\(\s*['\"]services-ngs-['\"]\s*\)\s*===\s*0\s*&&\s*href\s*===\s*['\"]services-ngs\.html['\"]\s*\)\s*a\.classList\.add\(\s*['\"]is-active['\"]\s*\);?\n?")
    pattern_dd = re.compile(r"if\s*\(\s*page\.indexOf\(\s*['\"]services-dd-['\"]\s*\)\s*===\s*0\s*&&\s*href\s*===\s*['\"]services-drug-discovery\.html['\"]\s*\)\s*a\.classList\.add\(\s*['\"]is-active['\"]\s*\);?\n?")
    pattern_cs = re.compile(r"if\s*\(\s*page\.indexOf\(\s*['\"]case-study-['\"]\s*\)\s*===\s*0\s*&&\s*href\s*===\s*['\"]case-studies\.html['\"]\s*\)\s*a\.classList\.add\(\s*['\"]is-active['\"]\s*\);?\n?")

    count = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        modified = False
        if pattern_ngs.search(content):
            content = pattern_ngs.sub("", content)
            modified = True
        if pattern_dd.search(content):
            content = pattern_dd.sub("", content)
            modified = True
        if pattern_cs.search(content):
            content = pattern_cs.sub("", content)
            modified = True
            
        if modified:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Fixed active navigation in: {os.path.basename(filepath)}")
            
    print(f"Completed! Updated {count} files.")

if __name__ == "__main__":
    main()
