import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
target_files = [f for f in os.listdir(workspace_dir) if f.endswith(".html")]

print(f"Checking {len(target_files)} files...")

for file_name in sorted(target_files):
    file_path = os.path.join(workspace_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    has_header_end = "</header>" in content
    has_footer_start = "<footer" in content
    has_script_start = "<script>" in content or "<script " in content
    
    if not (has_header_end and has_footer_start):
        print(f"ERROR: {file_name} lacks header_end or footer_start (Header end: {has_header_end}, Footer start: {has_footer_start})")
    else:
        # Test extraction
        try:
            header_end_idx = content.find("</header>") + len("</header>")
            footer_start_idx = content.find("<footer")
            main_content = content[header_end_idx:footer_start_idx].strip()
            
            # Find script after footer
            footer_end_idx = content.find("</footer>")
            script_content = ""
            if footer_end_idx != -1:
                script_start_idx = content.find("<script", footer_end_idx)
                if script_start_idx != -1:
                    script_content = content[script_start_idx:].strip()
            
            print(f"OK: {file_name} -> Content: {len(main_content)} chars, Script: {len(script_content)} chars")
        except Exception as e:
            print(f"ERROR: {file_name} failed extraction: {str(e)}")
