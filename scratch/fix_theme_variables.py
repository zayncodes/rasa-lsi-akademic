import os
import re

theme_path = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1\theme.css"

with open(theme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the first .rasa { that defines Brand palette variables
new_content, count1 = re.subn(
    r'\.rasa\s*\{\s*(/\*\s*Brand\s+palette\s*\*\/)',
    r'body.rasa {\n  \1',
    content
)

# Replace the second .rasa { that defines --glow-color, etc.
new_content, count2 = re.subn(
    r'\.rasa\s*\{\s*(--glow-color\s*:\s*rgba\(37,\s*99,\s*235,\s*0\.12\);)',
    r'body.rasa {\n  \1',
    new_content
)

print(f"Replaced brand palette .rasa: {count1} times")
print(f"Replaced glow .rasa: {count2} times")

with open(theme_path, "w", encoding="utf-8") as f:
    f.write(new_content)
