import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
overview_files = [
    "services-ngs.html",
    "services-drug-discovery.html"
]

tool_svgs = {}

# Regex to find: <div class="rasa-tool"><span class="rasa-tool__mono"><svg ...>...</svg></span><span class="rasa-tool__name">Name</span></div>
# Note: tags can span multiple lines, let's parse using a regular expression or simple state machine
tool_pattern = re.compile(
    r'<div\s+class="rasa-tool"\s*>\s*<span\s+class="rasa-tool__mono"\s*>\s*(<svg.*?</svg>)\s*</span>\s*<span\s+class="rasa-tool__name"\s*>(.*?)</span>\s*</div>',
    re.DOTALL | re.IGNORECASE
)

for file_name in overview_files:
    file_path = os.path.join(workspace_dir, file_name)
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = tool_pattern.findall(content)
    for svg, name in matches:
        name_clean = name.strip()
        tool_svgs[name_clean] = svg.strip()

print(f"Extracted {len(tool_svgs)} tool SVGs:")
for name in sorted(tool_svgs.keys()):
    print(f"- {name}")
