import os

source_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
theme_path = os.path.join(source_dir, "theme.css")

contact_btn_css = """
/* ==========================================================================
   Permanent Blue Styling for Contact/Partner Buttons
   ========================================================================== */
a.rasa-cta-btn[href*="contact"],
a.rasa-btn[href*="contact"],
a.rasa-svc-showcase__btn[href*="contact"],
.rasa-nav a.rasa-cta-btn[href*="contact"] {
  background: #2563eb !important;
  color: #ffffff !important;
  box-shadow: none !important;
  border: none !important;
  border-radius: 0.375rem !important;
  transition: background 0.2s, transform 0.2s !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}

a.rasa-cta-btn[href*="contact"]:hover,
a.rasa-btn[href*="contact"]:hover,
a.rasa-svc-showcase__btn[href*="contact"]:hover,
.rasa-nav a.rasa-cta-btn[href*="contact"]:hover {
  background: #1e40af !important;
  color: #ffffff !important;
  transform: translateY(-1px) !important;
  box-shadow: none !important;
}
"""

with open(theme_path, "a", encoding="utf-8") as f:
    f.write(contact_btn_css)

print("Appended permanent blue style for all contact buttons to theme.css")
