import re

def main():
    filepath = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1\index.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Replace chevron in Step 1
    # Check if we can do sequential replacements or precise replaces
    # We can match each step uniquely by its context
    
    # Step 1 Chevron
    step1_old = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--blue-up">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>"""
    step1_new = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--blue-down">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>"""

    # Step 2 Chevron
    step2_old = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--blue-down">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>"""
    step2_new = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--blue-up">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>"""

    # Step 3 Chevron
    step3_old = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-up">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>"""
    step3_new = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-down">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>"""

    # Step 4 Chevron
    step4_old = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-down">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>"""
    step4_new = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-up">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>"""

    # Step 5 Chevron
    step5_old = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-up">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>"""
    step5_new = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-down">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>"""

    # Step 6 Chevron
    step6_old = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-down">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </div>"""
    step6_new = """            <div class="rasa-workflow-chevron rasa-workflow-chevron--pink-up">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="18 15 12 9 6 15"></polyline></svg>
            </div>"""

    # We do them sequentially by replacing their specific occurrences in context
    # Since Step 1 has its content wrap first, then chevron, then circle
    # Step 2 has circle first, then chevron, then content wrap
    # We can use precise find-and-replace
    
    # We can identify the segments of HTML for each step and replace the chevron inside it
    # Step 1 block
    step1_block = re.search(r'<!-- Step 1: Client Challenge \(Top\) -->.*?<!-- Step 2:', content, re.DOTALL)
    if step1_block:
        new_step1_block = step1_block.group(0).replace(step1_old, step1_new)
        content = content.replace(step1_block.group(0), new_step1_block)

    # Step 2 block
    step2_block = re.search(r'<!-- Step 2: Solution Strategy \(Bottom\) -->.*?<!-- Step 3:', content, re.DOTALL)
    if step2_block:
        new_step2_block = step2_block.group(0).replace(step2_old, step2_new)
        content = content.replace(step2_block.group(0), new_step2_block)

    # Step 3 block
    step3_block = re.search(r'<!-- Step 3: Client Approval \(Top\) -->.*?<!-- Step 4:', content, re.DOTALL)
    if step3_block:
        new_step3_block = step3_block.group(0).replace(step3_old, step3_new)
        content = content.replace(step3_block.group(0), new_step3_block)

    # Step 4 block
    step4_block = re.search(r'<!-- Step 4: Go-Live on Project \(Bottom\) -->.*?<!-- Step 5:', content, re.DOTALL)
    if step4_block:
        new_step4_block = step4_block.group(0).replace(step4_old, step4_new)
        content = content.replace(step4_block.group(0), new_step4_block)

    # Step 5 block
    step5_block = re.search(r'<!-- Step 5: Project Updates \(Top\) -->.*?<!-- Step 6:', content, re.DOTALL)
    if step5_block:
        new_step5_block = step5_block.group(0).replace(step5_old, step5_new)
        content = content.replace(step5_block.group(0), new_step5_block)

    # Step 6 block
    step6_block = re.search(r'<!-- Step 6: Output & Delivery \(Bottom\) -->.*?</section>', content, re.DOTALL)
    if step6_block:
        new_step6_block = step6_block.group(0).replace(step6_old, step6_up_val := step6_new)
        # Note: step6_old is step6_old, step6_new is step6_new
        new_step6_block = step6_block.group(0).replace(step6_old, step6_new)
        content = content.replace(step6_block.group(0), new_step6_block)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Chevron replacement in index.html completed.")

if __name__ == "__main__":
    main()
