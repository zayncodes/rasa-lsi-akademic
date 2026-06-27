import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
target_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

external_scripts = []

for file_name in target_files:
    file_path = os.path.join(workspace_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Find all script tags with src
    srcs = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', content, re.IGNORECASE)
    if srcs:
        external_scripts.append((file_name, srcs))

print(f"Found external scripts in {len(external_scripts)} files:")
for fn, srcs in external_scripts:
    print(f"  {fn}: {srcs}")
