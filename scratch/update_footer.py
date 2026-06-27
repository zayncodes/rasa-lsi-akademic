import os
import re

source_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
html_files = [f for f in os.listdir(source_dir) if f.endswith(".html")]

target_block = """        <h4 style="margin-top:1.75rem;">QSAR &amp; Regulatory Toxicology</h4>
        <a href="services-qsar-toxicology.html">QSAR Toxicology &amp; ICH M7</a>
      </div>
      <div>
        <h4>Knowledge Base</h4>
        <a href="knowledge-base.html">Knowledge Base Overview</a>"""

replacement_block = """      </div>
      <div>
        <h4>QSAR &amp; Regulatory Toxicology</h4>
        <a href="services-qsar-toxicology.html">QSAR Toxicology &amp; ICH M7</a>
        <h4 style="margin-top:1.75rem;">Knowledge Base</h4>
        <a href="knowledge-base.html">Knowledge Base Overview</a>"""

modified_count = 0
for file_name in html_files:
    file_path = os.path.join(source_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find using regex that ignores whitespace variations and matches HTML entities
    pattern = re.compile(
        r'<\s*h4\s+style\s*=\s*["\']margin-top\s*:\s*1\.75rem\s*;?\s*["\']\s*>\s*QSAR\s*(?:&|&amp;)\s*Regulatory\s*Toxicology\s*<\s*/\s*h4\s*>\s*'
        r'<\s*a\s+href\s*=\s*["\']services-qsar-toxicology\.html["\']\s*>\s*QSAR\s*Toxicology\s*(?:&|&amp;)\s*ICH\s*M7\s*<\s*/\s*a\s*>\s*'
        r'<\s*/\s*div\s*>\s*'
        r'<\s*div\s*>\s*'
        r'<\s*h4\s*>\s*Knowledge\s*Base\s*<\s*/\s*h4\s*>\s*'
        r'<\s*a\s+href\s*=\s*["\']knowledge-base\.html["\']\s*>\s*Knowledge\s*Base\s*Overview\s*<\s*/\s*a\s*>',
        re.IGNORECASE
    )

    match = pattern.search(content)
    if match:
        content = content[:match.start()] + replacement_block + content[match.end():]
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        modified_count += 1
        # print(f"Updated footer in {file_name}")
    else:
        print(f"WARNING: Footer target block not found in {file_name}")

print(f"\nCompleted! Updated footer in {modified_count} of {len(html_files)} files.")
