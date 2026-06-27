import os
import re

source_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
theme_path = os.path.join(source_dir, "theme.css")
html_files = [f for f in os.listdir(source_dir) if f.endswith(".html")]

# 1. Append Mobile Menu CSS to theme.css
mobile_css = """
/* ==========================================================================
   RASA Mobile Navigation & Responsiveness Optimizations
   ========================================================================== */
.rasa-menu-toggle {
  display: none;
  background: transparent;
  border: none;
  color: var(--foreground-70);
  cursor: pointer;
  padding: 0.5rem;
  z-index: 1001;
  transition: color 0.2s, transform 0.2s;
}
.rasa-menu-toggle:hover {
  color: var(--leaf);
}
.rasa-menu-toggle__icon {
  width: 24px;
  height: 24px;
}
.rasa-menu-toggle__icon .line-top {
  transform-origin: 12px 6px;
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
.rasa-menu-toggle__icon .line-mid {
  transition: opacity 0.2s ease;
}
.rasa-menu-toggle__icon .line-bot {
  transform-origin: 12px 18px;
  transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}
body.menu-is-open .line-top {
  transform: translateY(6px) rotate(45deg);
}
body.menu-is-open .line-mid {
  opacity: 0;
}
body.menu-is-open .line-bot {
  transform: translateY(-6px) rotate(-45deg);
}

@media (max-width: 899px) {
  .rasa-menu-toggle {
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  
  body.menu-is-open .rasa-menu-toggle {
    color: var(--leaf);
  }
  
  .rasa-nav {
    display: flex !important;
    flex-direction: column !important;
    position: fixed !important;
    top: 64px !important;
    right: -100% !important;
    width: 320px !important;
    max-width: 85vw !important;
    height: calc(100vh - 64px) !important;
    background: var(--cream) !important;
    border-left: 1px solid var(--border) !important;
    padding: 2rem 1.5rem !important;
    gap: 1.25rem !important;
    overflow-y: auto !important;
    z-index: 1000 !important;
    transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
    box-shadow: -10px 0 30px rgba(15, 23, 42, 0.05) !important;
  }
  
  body.menu-is-open .rasa-nav {
    right: 0 !important;
  }
  
  .rasa-nav__item {
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: flex-start !important;
  }
  
  .rasa-nav__item > a {
    display: flex !important;
    justify-content: space-between !important;
    width: 100% !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    padding: 0.5rem 0 !important;
    border-bottom: 1px solid rgba(0,0,0,0.03) !important;
  }
  
  .rasa-nav__dropdown {
    display: none !important;
    position: static !important;
    opacity: 1 !important;
    visibility: visible !important;
    transform: none !important;
    box-shadow: none !important;
    background: transparent !important;
    border: none !important;
    padding: 0.5rem 0 0.5rem 1rem !important;
    flex-direction: column !important;
    gap: 0.85rem !important;
    width: 100% !important;
    pointer-events: auto !important;
    border-left: 1.5px solid var(--border) !important;
    margin-left: 0.25rem !important;
  }
  
  .rasa-nav__dropdown a {
    font-size: 0.95rem !important;
    padding: 0.25rem 0 !important;
    border: none !important;
  }
  
  .rasa-nav__subitem {
    position: relative !important;
    width: 100% !important;
    display: flex !important;
    flex-direction: column !important;
  }
  
  .rasa-nav__subitem > a {
    display: flex !important;
    justify-content: space-between !important;
    width: 100% !important;
  }
  
  .rasa-nav__subdropdown {
    display: none !important;
    position: static !important;
    opacity: 1 !important;
    visibility: visible !important;
    transform: none !important;
    box-shadow: none !important;
    background: transparent !important;
    border: none !important;
    padding: 0.5rem 0 0.5rem 1rem !important;
    flex-direction: column !important;
    gap: 0.85rem !important;
    width: 100% !important;
    pointer-events: auto !important;
    border-left: 1.5px solid var(--border) !important;
    margin-left: 0.25rem !important;
  }
  
  .rasa-nav__subdropdown a {
    font-size: 0.9rem !important;
    padding: 0.2rem 0 !important;
  }
  
  body.menu-is-open {
    overflow: hidden !important;
  }
}

@media (max-width: 480px) {
  .rasa-cta-btn {
    padding: 0.4rem 0.6rem !important;
    font-size: 0.8rem !important;
  }
  .rasa-cta-btn svg {
    display: none !important;
  }
  .rasa-brand img {
    height: 32px !important;
  }
}
"""

with open(theme_path, "a", encoding="utf-8") as f:
    f.write(mobile_css)
print("Appended mobile CSS to theme.css")

# 2. Add Mobile Toggle to Headers and Script Toggle to scripts in all HTML files
menu_btn_markup = """      <button class="rasa-menu-toggle" aria-label="Toggle Menu" aria-expanded="false">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="rasa-menu-toggle__icon"><line x1="3" y1="12" x2="21" y2="12" class="line-mid"/><line x1="3" y1="6" x2="21" y2="6" class="line-top"/><line x1="3" y1="18" x2="21" y2="18" class="line-bot"/></svg>
      </button>\n    """

mobile_js_script = """
  // Mobile menu toggle logic
  (function() {
    try {
      var toggle = document.querySelector('.rasa-menu-toggle');
      if (toggle) {
        toggle.addEventListener('click', function() {
          var expanded = toggle.getAttribute('aria-expanded') === 'true';
          toggle.setAttribute('aria-expanded', !expanded);
          document.body.classList.toggle('menu-is-open');
        });
      }
      // Expand/collapse dropdowns on mobile
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
      });
    } catch(e) {}
  })();
</script>
"""

modified_html_count = 0
for file_name in html_files:
    file_path = os.path.join(source_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Match actions div to inject hamburger button
    actions_pattern = re.compile(
        r'(<\s*div\s+class\s*=\s*["\']rasa-header__actions["\'].*?>\s*<\s*a\s+href\s*=\s*["\']contact\.html["\'].*?>.*?Partner\s+with\s+us.*?<\s*/\s*a\s*>\s*)(<\s*/\s*div\s*>)',
        re.DOTALL | re.IGNORECASE
    )
    
    # Check if button is already present first
    if "rasa-menu-toggle" not in content:
        content, c1 = actions_pattern.subn(r'\1' + menu_btn_markup + r'\2', content)
    else:
        c1 = 0

    # Inject JavaScript logic right before the last closing </script> tag
    if "Mobile menu toggle logic" not in content:
        # Find the last closing </script> tag
        script_idx = content.rfind("</script>")
        if script_idx != -1:
            content = content[:script_idx] + mobile_js_script + content[script_idx + len("</script>"):]
            c2 = 1
        else:
            c2 = 0
    else:
        c2 = 0

    if c1 > 0 or c2 > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        modified_html_count += 1

print(f"Completed! Injected mobile elements and logic in {modified_html_count} of {len(html_files)} files.")
