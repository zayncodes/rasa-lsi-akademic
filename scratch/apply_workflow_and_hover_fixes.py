import os
import re

theme_path = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1\theme.css"

with open(theme_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Partner with us button - make it permanently blue
# Let's find the original .rasa-cta-btn and replace it
original_cta_pattern = re.compile(
    r'\.rasa-cta-btn\s*\{\s*display:\s*inline-flex;\s*align-items:\s*center;\s*gap:\s*0.5rem;\s*background:\s*var\(--leaf\);\s*color:\s*var\(--cream\);\s*font-size:\s*0.875rem;\s*font-weight:\s*500;\s*padding:\s*0.5rem\s*0.5rem\s*0.5rem\s*0.75rem;\s*border-radius:\s*0.4rem;\s*box-shadow:\s*inset\s*0\s*0\s*0\s*1px\s*rgba\(37,\s*99,\s*235,\s*0.8\);\s*transition:\s*background\s*0.2s,\s*transform\s*0.2s;\s*\}',
    re.IGNORECASE
)

new_cta_style = """.rasa-cta-btn {
  display: inline-flex; align-items: center; gap: 0.5rem;
  background: #2563eb !important; color: #f8fafc !important;
  font-size: 0.875rem; font-weight: 500;
  padding: 0.5rem 0.5rem 0.5rem 0.75rem; border-radius: 0.4rem;
  box-shadow: inset 0 0 0 1px rgba(37, 99, 235, 0.8) !important;
  transition: background 0.2s, transform 0.2s;
}"""

content, c1 = original_cta_pattern.subn(new_cta_style, content)

# Also update the cta button hover
original_cta_hover_pattern = re.compile(
    r'\.rasa-cta-btn:hover\s*\{\s*background:\s*var\(--leaf-hover\);\s*transform:\s*translateY\(-1px\);\s*\}',
    re.IGNORECASE
)

new_cta_hover_style = """.rasa-cta-btn:hover { background: #1d4ed8 !important; transform: translateY(-1px); }"""
content, c2 = original_cta_hover_pattern.subn(new_cta_hover_style, content)

# 2. Background hover glow on capability cards:
# First, remove !important from .rasa-capability::before in lines 610-618
original_cap_before = """.rasa-capability::before {
  content: "" !important;
  position: absolute !important;
  top: 0 !important; left: 0 !important;
  width: 100% !important; height: 3px !important;
  background: linear-gradient(90deg, var(--leaf-soft), var(--leaf)) !important;
  opacity: 0 !important;
  transition: opacity 0.3s ease !important;
}"""

# Normalize spaces for match
normalized_content = re.sub(
    r'\.rasa-capability::before\s*\{\s*content:\s*""\s*!important;\s*position:\s*absolute\s*!important;\s*top:\s*0\s*!important;\s*left:\s*0\s*!important;\s*width:\s*100%\s*!important;\s*height:\s*3px\s*!important;\s*background:\s*linear-gradient\(90deg,\s*var\(--leaf-soft\),\s*var\(--leaf\)\)\s*!important;\s*opacity:\s*0\s*!important;\s*transition:\s*opacity\s*0.3s\s*ease\s*!important;\s*\}',
    """.rasa-capability::before {
  content: "";
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 3px;
  background: linear-gradient(90deg, var(--leaf-soft), var(--leaf));
  opacity: 0;
  transition: opacity 0.3s ease;
}""",
    content
)

# 3. Add !important to placement properties in line 3612-3621 (interactive cards glow)
original_interactive_before = re.compile(
    r'\.rasa-svc-card::before,\s*\.rasa-capability::before,\s*\.rasa-check::before,\s*\.rasa-card::before,\s*\.rasa-tab-btn::before,\s*\.rasa-highlight::before\s*\{\s*'
    r'content:\s*\'\'\s*!important;\s*'
    r'position:\s*absolute\s*!important;\s*'
    r'top:\s*0;\s*left:\s*0;\s*width:\s*100%;\s*height:\s*100%;\s*'
    r'background:\s*radial-gradient\(300px\s*circle\s*at\s*var\(--mouse-x,\s*0px\)\s*var\(--mouse-y,\s*0px\),\s*var\(--glow-color\),\s*transparent\s*45%\)\s*!important;\s*'
    r'z-index:\s*-1\s*!important;\s*'
    r'pointer-events:\s*none\s*!important;\s*'
    r'opacity:\s*0\s*!important;\s*'
    r'transition:\s*opacity\s*0.4s\s*ease\s*!important;\s*\}',
    re.IGNORECASE
)

new_interactive_before = """.rasa-svc-card::before, .rasa-capability::before, .rasa-check::before, .rasa-card::before, .rasa-tab-btn::before, .rasa-highlight::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important; left: 0 !important; width: 100% !important; height: 100% !important;
  background: radial-gradient(300px circle at var(--mouse-x, 0px) var(--mouse-y, 0px), var(--glow-color), transparent 45%) !important;
  z-index: -1 !important;
  pointer-events: none !important;
  opacity: 0 !important;
  transition: opacity 0.4s ease !important;
}"""

normalized_content, c3 = original_interactive_before.subn(new_interactive_before, normalized_content)

# 4. Workflow step 2, 4, 6 bubbles offset adjustments
# Change .rasa-workflow-col--bottom .rasa-workflow-circle top from 265px to 285px
circle_bottom_pattern = re.compile(
    r'(\.rasa-workflow-col--bottom\s+\.rasa-workflow-circle\s*\{\s*position:\s*absolute;\s*top:\s*)265px(;\s*left:\s*50%;\s*transform:\s*translateX\(-50%\);\s*\})',
    re.IGNORECASE
)
normalized_content, c4 = circle_bottom_pattern.subn(r'\g<1>285px\g<2>', normalized_content)

# Change .rasa-workflow-col--bottom .rasa-workflow-chevron top from 200px to 220px
chevron_bottom_pattern = re.compile(
    r'(\.rasa-workflow-col--bottom\s+\.rasa-workflow-chevron\s*\{\s*position:\s*absolute;\s*top:\s*)200px(;\s*left:\s*50%;\s*transform:\s*translateX\(-50%\);\s*color:\s*var\(--chevron-color\);\s*animation:\s*bounceUp\s*2\.5s\s*infinite\s*ease-in-out;\s*\})',
    re.IGNORECASE
)
normalized_content, c5 = chevron_bottom_pattern.subn(r'\g<1>220px\g<2>', normalized_content)

print(f"Partner CTA style modified: {c1}")
print(f"Partner CTA hover style modified: {c2}")
print(f"Interactive card glow style modified: {c3}")
print(f"Workflow circle top modified: {c4}")
print(f"Workflow chevron top modified: {c5}")

with open(theme_path, "w", encoding="utf-8") as f:
    f.write(normalized_content)
