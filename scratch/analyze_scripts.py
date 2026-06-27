import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
target_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

for file_name in sorted(target_files):
    file_path = os.path.join(workspace_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    footer_end_idx = content.find("</footer>")
    if footer_end_idx != -1:
        after_footer = content[footer_end_idx:]
        scripts = re.findall(r"<script.*?>.*?</script>", after_footer, re.DOTALL)
        print(f"{file_name}: found {len(scripts)} script blocks after footer")
        for i, s in enumerate(scripts):
            print(f"  Script {i+1}: {s[:100]} ... {s[-100:]}")
