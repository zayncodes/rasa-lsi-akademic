import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
target_files = [
    # 10 NGS subpages
    "services-ngs-transcriptomics.html",
    "services-ngs-single-cell.html",
    "services-ngs-wgs-wes.html",
    "services-ngs-spatial.html",
    "services-ngs-metagenomics.html",
    "services-ngs-epigenomics.html",
    "services-ngs-long-read.html",
    "services-ngs-multi-omics.html",
    "services-ngs-clinical.html",
    "services-ngs-biomarker.html",
    # 7 DD subpages
    "services-dd-target-id.html",
    "services-dd-virtual-screening.html",
    "services-dd-molecular-dynamics.html",
    "services-dd-protein-modeling.html",
    "services-dd-de-novo.html",
    "services-dd-multi-target.html",
    "services-dd-lead-optimization.html"
]

all_tools = set()

for file_name in target_files:
    file_path = os.path.join(workspace_dir, file_name)
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Find all rasa-tool__name content
    matches = re.findall(r'class="rasa-tool__name"\s*>(.*?)</span>', content)
    for m in matches:
        all_tools.add(m.strip())

print("Found tools:")
for t in sorted(all_tools):
    print(f"- {t}")
