import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
target_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

external_css = []

for file_name in target_files:
    file_path = os.path.join(workspace_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all link tags with href ending in .css
    hrefs = re.findall(r'<link[^>]+href=["\']([^"\']+\.css[^"\']*)["\']', content, re.IGNORECASE)
    if hrefs:
        # Filter out Google Fonts or other CDNs
        local_css = [h for h in hrefs if not h.startswith("http") and not h.startswith("//")]
        if local_css:
            external_css.append((file_name, local_css))

print(f"Found local CSS in {len(external_css)} files:")
for fn, hrefs in external_css:
    print(f"  {fn}: {hrefs}")
