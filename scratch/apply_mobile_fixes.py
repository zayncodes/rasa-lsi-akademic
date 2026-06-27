import os
import re

source_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
theme_path = os.path.join(source_dir, "theme.css")
html_files = [f for f in os.listdir(source_dir) if f.endswith(".html")]

# 1. Update theme.css with mobile fixes
with open(theme_path, "r", encoding="utf-8") as f:
    theme_content = f.read()

# Add z-index: 2 !important to .rasa-workflow-col and .rasa-workflow-circle in max-width media query
# Let's locate the max-width: 1000px query block or append it to the very end of theme.css
mobile_css_fixes = """
/* ==========================================================================
   Mobile Fixes: Disable Stuck Hover Transforms & Enable CSS Dropdowns
   ========================================================================== */
@media (max-width: 899px) {
  /* Prevent horizontal overflow scrolling globally on mobile */
  html, body {
    max-width: 100% !important;
    overflow-x: hidden !important;
  }

  /* Disable hover transform transitions and lifts on mobile to prevent cards getting stuck */
  .rasa-svc-card:hover,
  .rasa-capability:hover,
  .rasa-check:hover,
  .rasa-card:hover,
  .rasa-tab-btn:hover,
  .rasa-highlight:hover,
  .rasa-tool:hover,
  .rasa-techcat:hover,
  .rasa-workflow-circle:hover {
    transform: none !important;
    box-shadow: none !important;
    border-color: var(--border) !important;
  }
  
  /* Disable hover glow on mobile */
  .rasa-svc-card:hover::before,
  .rasa-capability:hover::before,
  .rasa-check:hover::before,
  .rasa-card:hover::before,
  .rasa-tab-btn:hover::before,
  .rasa-highlight:hover::before {
    opacity: 0 !important;
  }
  
  /* Expand dropdowns when active */
  .rasa-nav__item.is-active .rasa-nav__dropdown {
    display: flex !important;
  }
  .rasa-nav__subitem.is-active .rasa-nav__subdropdown {
    display: flex !important;
  }
  
  /* Prevent browser focus outlines on mobile buttons and links */
  .rasa-nav a:focus,
  .rasa-nav__item > a:focus,
  .rasa-nav__dropdown a:focus,
  .rasa-menu-toggle:focus {
    outline: none !important;
    border-color: transparent !important;
    box-shadow: none !important;
  }
}

@media (max-width: 1000px) {
  /* Fix Workflow dotted line crossing circles on mobile */
  .rasa-workflow-col {
    z-index: 2 !important;
  }
  .rasa-workflow-circle {
    z-index: 2 !important;
    background: #ffffff !important;
  }
  .rasa-workflow-col--top .rasa-workflow-circle,
  .rasa-workflow-col--bottom .rasa-workflow-circle {
    z-index: 2 !important;
    background: #ffffff !important;
  }
}
"""

with open(theme_path, "a", encoding="utf-8") as f:
    f.write(mobile_css_fixes)
print("Appended mobile fixes CSS to theme.css")


# 2. Update JavaScript in all HTML files
modified_count = 0
for file_name in html_files:
    file_path = os.path.join(source_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace the mobile menu toggle logic JS
    old_menu_js = """      // Expand/collapse dropdowns on mobile
      document.querySelectorAll('.rasa-nav__item > a').forEach(function(link) {
        link.addEventListener('click', function(e) {
          if (window.innerWidth < 900 && link.nextElementSibling && link.nextElementSibling.classList.contains('rasa-nav__dropdown')) {
            e.preventDefault();
            var parent = link.parentElement;
            parent.classList.toggle('is-active');
            var dropdown = link.nextElementSibling;
            if (dropdown.style.display === 'flex') {
              dropdown.style.display = 'none';
            } else {
              dropdown.style.display = 'flex';
            }
          }
        });
      });
      // Expand/collapse sub-dropdowns on mobile
      document.querySelectorAll('.rasa-nav__subitem > a').forEach(function(link) {
        link.addEventListener('click', function(e) {
          if (window.innerWidth < 900 && link.nextElementSibling && link.nextElementSibling.classList.contains('rasa-nav__subdropdown')) {
            e.preventDefault();
            var parent = link.parentElement;
            parent.classList.toggle('is-active');
            var dropdown = link.nextElementSibling;
            if (dropdown.style.display === 'flex') {
              dropdown.style.display = 'none';
            } else {
              dropdown.style.display = 'flex';
            }
          }
        });
      });"""

    new_menu_js = """      // Expand/collapse dropdowns on mobile
      document.querySelectorAll('.rasa-nav__item > a').forEach(function(link) {
        link.addEventListener('click', function(e) {
          if (window.innerWidth < 900 && link.nextElementSibling && link.nextElementSibling.classList.contains('rasa-nav__dropdown')) {
            e.preventDefault();
            var parent = link.parentElement;
            parent.classList.toggle('is-active');
          }
        });
      });
      // Expand/collapse sub-dropdowns on mobile
      document.querySelectorAll('.rasa-nav__subitem > a').forEach(function(link) {
        link.addEventListener('click', function(e) {
          if (window.innerWidth < 900 && link.nextElementSibling && link.nextElementSibling.classList.contains('rasa-nav__subdropdown')) {
            e.preventDefault();
            var parent = link.parentElement;
            parent.classList.toggle('is-active');
          }
        });
      });"""

    content = content.replace(old_menu_js, new_menu_js)

    # Disable 3D tilt on mobile
    old_tilt_mousemove = """    card.addEventListener('mousemove', function (e) {
      if ((card.classList.contains('rasa-svc-showcase__btn') || card.classList.contains('rasa-check')) && window.innerWidth <= 992) {
        return;
      }"""

    new_tilt_mousemove = """    card.addEventListener('mousemove', function (e) {
      if (window.innerWidth < 900) {
        return;
      }
      if ((card.classList.contains('rasa-svc-showcase__btn') || card.classList.contains('rasa-check')) && window.innerWidth <= 992) {
        return;
      }"""

    content = content.replace(old_tilt_mousemove, new_tilt_mousemove)

    old_tilt_mouseleave = """    card.addEventListener('mouseleave', function () {
      if ((card.classList.contains('rasa-svc-showcase__btn') || card.classList.contains('rasa-check')) && window.innerWidth <= 992) {
        return;
      }"""

    new_tilt_mouseleave = """    card.addEventListener('mouseleave', function () {
      if (window.innerWidth < 900) {
        return;
      }
      if ((card.classList.contains('rasa-svc-showcase__btn') || card.classList.contains('rasa-check')) && window.innerWidth <= 992) {
        return;
      }"""

    content = content.replace(old_tilt_mouseleave, new_tilt_mouseleave)

    # Also for index.html signature workflow circles:
    old_workflow_mousemove = """    circle.addEventListener('mousemove', function (e) {
      var rect = circle.getBoundingClientRect();"""
    new_workflow_mousemove = """    circle.addEventListener('mousemove', function (e) {
      if (window.innerWidth < 900) return;
      var rect = circle.getBoundingClientRect();"""
    content = content.replace(old_workflow_mousemove, new_workflow_mousemove)

    old_workflow_mouseleave = """    circle.addEventListener('mouseleave', function () {
      circle.style.removeProperty('transform');"""
    new_workflow_mouseleave = """    circle.addEventListener('mouseleave', function () {
      if (window.innerWidth < 900) return;
      circle.style.removeProperty('transform');"""
    content = content.replace(old_workflow_mouseleave, new_workflow_mouseleave)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    modified_count += 1

print(f"Updated JS logic in {modified_count} of {len(html_files)} files.")
