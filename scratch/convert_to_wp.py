import os
import re
import shutil

# Paths
source_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
target_dir = r"C:\Users\Nilesh\Desktop\RASALSI\RasaWP"

# Create target directory if it doesn't exist
os.makedirs(target_dir, exist_ok=True)

# Copy Assets
print("Copying global assets...")
# Copy theme.css to global-styles.css
theme_src = os.path.join(source_dir, "theme.css")
theme_dst = os.path.join(target_dir, "global-styles.css")
shutil.copy2(theme_src, theme_dst)
print(f"Copied theme.css -> global-styles.css")

# Copy logo.png
logo_src = os.path.join(source_dir, "logo.png")
logo_dst = os.path.join(target_dir, "logo.png")
if os.path.exists(logo_src):
    shutil.copy2(logo_src, logo_dst)
    print("Copied logo.png")

# Copy favicon.svg
fav_src = os.path.join(source_dir, "favicon.svg")
fav_dst = os.path.join(target_dir, "favicon.svg")
if os.path.exists(fav_src):
    shutil.copy2(fav_src, fav_dst)
    print("Copied favicon.svg")

# Copy images/ directory recursively
images_src_dir = os.path.join(source_dir, "images")
images_dst_dir = os.path.join(target_dir, "images")
if os.path.exists(images_src_dir):
    if os.path.exists(images_dst_dir):
        shutil.rmtree(images_dst_dir)
    shutil.copytree(images_src_dir, images_dst_dir)
    print("Copied images/ directory recursively")

# Get all HTML files
html_files = [f for f in os.listdir(source_dir) if f.endswith(".html")]
print(f"Found {len(html_files)} HTML files to convert.")

def optimize_paths(content):
    # 1. Replace index.html (and with optional anchor)
    # Match href="index.html" or href='index.html' or href="index.html#section"
    # Group 1: opening quote, Group 2: optional anchor name
    content = re.sub(
        r'href=(["\'])index\.html(?:#([a-zA-Z0-9\-_]+))?\1',
        lambda m: f'href={m.group(1)}/{ "#" + m.group(2) if m.group(2) else ""}{m.group(1)}',
        content
    )

    # 2. Replace other internal links to HTML files (and with optional anchor)
    # Match href="page.html" or href="page.html#section"
    # Avoid matching absolute/protocol URLs
    def replace_subpage(m):
        quote = m.group(1)
        page = m.group(2)
        anchor = m.group(3)
        anchor_str = f"#{anchor}" if anchor else ""
        return f'href={quote}/{page}/{anchor_str}{quote}'

    content = re.sub(
        r'href=(["\'])(?!index)([a-zA-Z0-9\-_]+)\.html(?:#([a-zA-Z0-9\-_]+))?\1',
        replace_subpage,
        content
    )

    # 3. Replace relative asset paths with root-relative paths
    # Match images/ prefixed by quote, space, paren, or comma
    content = re.sub(r'(?<=["\'(\s,])images/', '/images/', content)
    # Match logo.png prefixed by quote, space, paren, or comma
    content = re.sub(r'(?<=["\'(\s,])logo\.png', '/logo.png', content)
    # Match favicon.svg prefixed by quote, space, paren, or comma
    content = re.sub(r'(?<=["\'(\s,])favicon\.svg', '/favicon.svg', content)

    return content

converted_count = 0
for file_name in sorted(html_files):
    file_path = os.path.join(source_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Search for header and footer boundaries case-insensitively
    header_match = re.search(r'</header>', content, re.IGNORECASE)
    footer_match = re.search(r'<footer', content, re.IGNORECASE)

    if not (header_match and footer_match):
        print(f"WARNING: Skipping {file_name} because </header> or <footer was not found.")
        continue

    # Extract body content
    body_content = content[header_match.end():footer_match.start()].strip()

    # Extract scripts after the footer
    footer_end_match = re.search(r'</footer>', content, re.IGNORECASE)
    script_blocks = []
    if footer_end_match:
        after_footer = content[footer_end_match.end():]
        script_blocks = re.findall(r'<script.*?>.*?</script>', after_footer, re.DOTALL | re.IGNORECASE)

    # Combine body content and script blocks
    combined_snippet = body_content
    if script_blocks:
        combined_snippet += "\n\n" + "\n\n".join(script_blocks)

    # Run optimization replacements
    optimized_snippet = optimize_paths(combined_snippet)

    # Save to target directory
    target_file_path = os.path.join(target_dir, file_name)
    with open(target_file_path, "w", encoding="utf-8") as f:
        f.write(optimized_snippet)

    converted_count += 1
    # print(f"Successfully converted: {file_name}")

print(f"\nCompleted! Converted {converted_count} of {len(html_files)} files into {target_dir}")
