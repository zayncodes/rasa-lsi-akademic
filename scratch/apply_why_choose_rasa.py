import os

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"

why_choose_section = """<section class="rasa-section" style="padding:5rem 0; border-top:1px solid var(--border);">
  <div class="container">
    <div class="rasa-reveal" style="margin-bottom:3rem;">
      <span class="rasa-eyebrow">Why RASA</span>
      <h2 class="rasa-h2" style="margin-top:1.25rem;">Why Choose RASA?</h2>
    </div>
    <div class="rasa-svc-grid">
    <article class="rasa-svc-card rasa-reveal">
      <span class="rasa-svc-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.2l1.9 4.4 4.4 1.9-4.4 1.9L12 15.8l-1.9-4.4L5.7 9.5l4.4-1.9z"/><circle cx="18.5" cy="17.5" r="1.4"/><circle cx="5.5" cy="17" r="1.2"/></svg></span>
      <h3 class="rasa-svc-card__h">AI-Assisted Bioinformatics</h3>
      <p class="rasa-svc-card__b">Machine learning-enabled workflows for biomarker discovery, variant prioritization, and predictive genomics.</p>
    </article>
    <article class="rasa-svc-card rasa-reveal">
      <span class="rasa-svc-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 2.5 7 12 11.5 21.5 7z"/><path d="M2.5 12 12 16.5 21.5 12M2.5 16.5 12 21l9.5-4.5"/></svg></span>
      <h3 class="rasa-svc-card__h">Multi-Platform Expertise</h3>
      <p class="rasa-svc-card__b">Support for Illumina, Oxford Nanopore, PacBio HiFi, and 10x Genomics platforms.</p>
    </article>
    <article class="rasa-svc-card rasa-reveal">
      <span class="rasa-svc-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 2.5 7 12 11.5 21.5 7z"/><path d="M2.5 12 12 16.5 21.5 12M2.5 16.5 12 21l9.5-4.5"/></svg></span>
      <h3 class="rasa-svc-card__h">End-to-End Analysis</h3>
      <p class="rasa-svc-card__b">From raw sequencing data to biological interpretation and publication-ready reports.</p>
    </article>
    <article class="rasa-svc-card rasa-reveal">
      <span class="rasa-svc-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="6.5" cy="7" r="2.6"/><circle cx="17.5" cy="9" r="2.6"/><circle cx="10.5" cy="17.5" r="2.6"/><path d="M8.8 8.4l6.8 1.2M8.3 9.5l2.6 6"/></svg></span>
      <h3 class="rasa-svc-card__h">Cloud-Ready Infrastructure</h3>
      <p class="rasa-svc-card__b">Deployable on AWS, Google Cloud, HPC clusters, and secure on-premise environments.</p>
    </article>
    <article class="rasa-svc-card rasa-reveal">
      <span class="rasa-svc-card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 2.5 2.5 7 12 11.5 21.5 7z"/><path d="M2.5 12 12 16.5 21.5 12M2.5 16.5 12 21l9.5-4.5"/></svg></span>
      <h3 class="rasa-svc-card__h">Reproducible Workflows</h3>
      <p class="rasa-svc-card__b">Built using Nextflow, Snakemake, Docker, and Singularity for enterprise-grade bioinformatics operations.</p>
    </article>
    </div>
  </div>
</section>"""

target_files = [
    # 10 NGS subpages
    "services-ngs-transcriptomics.html",
    "services-ngs-single-cell.html",
    "services-ngs-wgs-wes.html",
    "services-ngs-spatial.html",
    "services-ngs-metagenomics.html",
    "services-ngs-epigenomics.html",
    "services-ngs-long-read.html",
    "services-ngs-multi-omics.html",
    "services-ngs-clinical.html",
    "services-ngs-biomarker.html",
    # 7 DD subpages
    "services-dd-target-id.html",
    "services-dd-virtual-screening.html",
    "services-dd-molecular-dynamics.html",
    "services-dd-protein-modeling.html",
    "services-dd-de-novo.html",
    "services-dd-multi-target.html",
    "services-dd-lead-optimization.html"
]

def process_file(file_name):
    file_path = os.path.join(workspace_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Search for "Why Choose RASA?" or "Why Choose RASA"
    index = content.find("Why Choose RASA")
    if index != -1:
        # Locate start and end of the enclosing <section>
        start_sec = content.rfind("<section", 0, index)
        end_sec = content.find("</section>", index)
        if start_sec != -1 and end_sec != -1:
            end_sec += len("</section>")
            old_section = content[start_sec:end_sec]
            # Replace it
            new_content = content.replace(old_section, why_choose_section)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated section in {file_name}")
            return True
        else:
            print(f"Found keyword but failed to locate section boundaries in {file_name}")
            return False
    else:
        # File doesn't have it, insert it
        if "molecular-dynamics" in file_name:
            # Insert before FAQ section
            faq_index = content.find("Frequently Asked Questions")
            if faq_index == -1:
                faq_index = content.find("Service FAQ")
            if faq_index != -1:
                start_sec = content.rfind("<section", 0, faq_index)
                if start_sec != -1:
                    new_content = content[:start_sec] + why_choose_section + "\n\n" + content[start_sec:]
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Inserted section in {file_name}")
                    return True
            print(f"Failed to find FAQ section in {file_name}")
            return False
        elif "lead-optimization" in file_name:
            # Insert before CTA section
            cta_index = content.find("rasa-section--ink")
            if cta_index == -1:
                cta_index = content.find("Accelerate therapeutic discovery")
            if cta_index != -1:
                start_sec = content.rfind("<section", 0, cta_index)
                if start_sec != -1:
                    new_content = content[:start_sec] + why_choose_section + "\n\n" + content[start_sec:]
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Inserted section in {file_name}")
                    return True
            print(f"Failed to find CTA section in {file_name}")
            return False
        else:
            print(f"No Why Choose section and no insertion rule for {file_name}")
            return False

def main():
    success = 0
    failed = 0
    for name in target_files:
        if process_file(name):
            success += 1
        else:
            failed += 1
    print(f"Process complete. Success: {success}, Failed: {failed}")

if __name__ == "__main__":
    main()
