import os
import re

target_dir = r"C:\Users\Nilesh\Desktop\RASALSI\RasaWP"

# 1. Check folder existence
assert os.path.exists(target_dir), "Target directory does not exist!"

# 2. Check file counts
target_files = os.listdir(target_dir)
html_files = [f for f in target_files if f.endswith(".html")]
print(f"Total HTML files in RasaWP: {len(html_files)}")
assert len(html_files) == 43, f"Expected 43 HTML files, found {len(html_files)}"

# 3. Check assets
assert "global-styles.css" in target_files, "global-styles.css is missing!"
assert "logo.png" in target_files, "logo.png is missing!"
assert "favicon.svg" in target_files, "favicon.svg is missing!"
assert "images" in target_files, "images folder is missing!"

images_dir = os.path.join(target_dir, "images")
image_files = os.listdir(images_dir)
print(f"Total image files in RasaWP/images: {len(image_files)}")
assert len(image_files) == 32, f"Expected 32 images, found {len(image_files)}"

# 4. Spot check a few files
spot_checks = ["index.html", "about.html", "services-ngs-spatial.html"]
for name in spot_checks:
    file_path = os.path.join(target_dir, name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    print(f"\nVerifying {name}...")
    
    # Header check
    assert "<header" not in content.lower(), f"Header tag found in {name}!"
    assert "</header>" not in content.lower(), f"Header closing tag found in {name}!"
    
    # Footer check
    assert "<footer" not in content.lower(), f"Footer tag found in {name}!"
    assert "</footer>" not in content.lower(), f"Footer closing tag found in {name}!"
    
    # Script check
    scripts = re.findall(r"<script.*?>.*?</script>", content, re.DOTALL | re.IGNORECASE)
    print(f"  Found {len(scripts)} script tags in snippet.")
    assert len(scripts) > 0, f"No script tags found in {name} snippet!"
    
    # Link check
    original_links = re.findall(r'href=["\'][a-zA-Z0-9\-_]+\.html', content, re.IGNORECASE)
    print(f"  Found original .html links: {original_links}")
    assert len(original_links) == 0, f"Found unresolved relative .html links in {name}: {original_links}"
    
    # Asset path check
    # Check if there is any images/ (without preceding /)
    # Match images/ not preceded by / or another directory
    unresolved_images = re.findall(r'(?<!/)(?<![a-zA-Z0-9\-_])images/', content)
    print(f"  Unresolved images/ paths: {unresolved_images}")
    assert len(unresolved_images) == 0, f"Found unresolved images/ paths in {name}!"
    
    # Check if there is any logo.png (without preceding /)
    unresolved_logo = re.findall(r'(?<!/)logo\.png', content)
    print(f"  Unresolved logo.png paths: {unresolved_logo}")
    assert len(unresolved_logo) == 0, f"Found unresolved logo.png paths in {name}!"

print("\nAll verifications passed successfully!")
