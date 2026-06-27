import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"

# The standardized active nav detection script
standardized_script = """  // Active navigation link detection
  try {
    var path = window.location.pathname;
    var page = path.split('/').pop();
    if (!page || page === '') page = 'index.html';
    document.querySelectorAll('.rasa-nav a').forEach(function (a) {
      a.classList.remove('is-active');
      var href = (a.getAttribute('href') || '').split('#')[0].split('/').pop();
      var pageClean = page.replace(/\\.html$/, '');
      var hrefClean = href.replace(/\\.html$/, '');
      if (hrefClean === pageClean) a.classList.add('is-active');
    });
  } catch (e) {}"""

def update_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to find the try-catch block containing document.querySelectorAll('.rasa-nav a')
    # A robust regex to find the try/catch block containing '.rasa-nav a'
    # We match: try { ... document.querySelectorAll('.rasa-nav a') ... } catch (e) {}
    # Since there are variations, we search for this specific block:
    
    pattern = re.compile(
        r'(\s*//\s*Active navigation link detection)?\s*try\s*\{[^{}]*document\.querySelectorAll\(\'\.rasa-nav a\'\).*?\}\s*catch\s*\(e\)\s*\{\}',
        re.DOTALL
    )
    
    # Let's see if we can find it
    match = pattern.search(content)
    if match:
        matched_str = match.group(0)
        # Replace the matched section with the standardized script
        new_content = content.replace(matched_str, "\n" + standardized_script)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {os.path.basename(file_path)}")
        return True
    else:
        # Try a simpler match if the comment is missing or structure is slightly different
        pattern_alt = re.compile(
            r'\s*try\s*\{[^{}]*document\.querySelectorAll\(\'\.rasa-nav a\'\).*?\}\s*catch\s*\(e\)\s*\{\}',
            re.DOTALL
        )
        match_alt = pattern_alt.search(content)
        if match_alt:
            matched_str = match_alt.group(0)
            new_content = content.replace(matched_str, "\n" + standardized_script)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated (alt): {os.path.basename(file_path)}")
            return True
        else:
            print(f"Failed to find match in: {os.path.basename(file_path)}")
            return False

def main():
    success_count = 0
    failure_count = 0
    for root, dirs, files in os.walk(workspace_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                if update_html_file(file_path):
                    success_count += 1
                else:
                    failure_count += 1
    print(f"Finished. Success: {success_count}, Failures: {failure_count}")

if __name__ == '__main__':
    main()
