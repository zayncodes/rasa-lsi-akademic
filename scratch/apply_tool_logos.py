import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"
overview_files = [
    "services-ngs.html",
    "services-drug-discovery.html"
]

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

tool_svgs = {}

# Regex to extract SVGs from overview pages
tool_pattern_extract = re.compile(
    r'<div\s+class="rasa-tool"\s*>\s*<span\s+class="rasa-tool__mono"\s*>\s*(<svg.*?</svg>)\s*</span>\s*<span\s+class="rasa-tool__name"\s*>(.*?)</span>\s*</div>',
    re.DOTALL | re.IGNORECASE
)

for file_name in overview_files:
    file_path = os.path.join(workspace_dir, file_name)
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    matches = tool_pattern_extract.findall(content)
    for svg, name in matches:
        tool_svgs[name.strip()] = svg.strip()

# Fallback SVGs
fallbacks = {
    "aws": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 7l10 5 10-5-10-5z" fill="#FF9900"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5" stroke="#FF9900" stroke-width="1.5"/></svg>',
    "gcp": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L3 7v10l9 5 9-5V7l-9-5z" stroke="#4285F4" stroke-width="1.5"/><circle cx="12" cy="12" r="3" fill="#4285F4"/></svg>',
    "hpc": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="3" width="18" height="5" rx="1" fill="#455A64"/><rect x="3" y="10" width="18" height="5" rx="1" fill="#455A64"/><rect x="3" y="17" width="18" height="5" rx="1" fill="#455A64"/><circle cx="6" cy="5.5" r="1" fill="#00E676"/><circle cx="6" cy="12.5" r="1" fill="#00E676"/><circle cx="6" cy="19.5" r="1" fill="#00E676"/></svg>',
    "chart": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 3V21H21" stroke="#3F51B5" stroke-width="2" stroke-linecap="round"/><path d="M7 14l4-4 5 5 4-7" stroke="#FF1744" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>',
    "bacteria": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="#00796B" stroke-width="1.5"/><circle cx="9" cy="10" r="1.5" fill="#00796B"/><circle cx="15" cy="11" r="2" fill="#00796B"/><circle cx="12" cy="15" r="1" fill="#00796B"/></svg>',
    "network": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="5" r="2.5" fill="#7E57C2"/><circle cx="7" cy="14" r="2.5" fill="#7E57C2"/><circle cx="17" cy="14" r="2.5" fill="#7E57C2"/><line x1="12" y1="7.5" x2="7.5" y2="11.5" stroke="#7E57C2" stroke-width="1.5"/><line x1="12" y1="7.5" x2="16.5" y2="11.5" stroke="#7E57C2" stroke-width="1.5"/><line x1="9.5" y1="14" x2="14.5" y2="14" stroke="#7E57C2" stroke-width="1.5"/></svg>',
    "dna": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.5 10.5C4.5 10.5 8 3 12 3C16 3 19.5 10.5 19.5 10.5M4.5 13.5C4.5 13.5 8 21 12 21C16 21 19.5 13.5 19.5 13.5" stroke="#E53935" stroke-width="1.5"/><line x1="7" y1="7" x2="7" y2="17" stroke="#E53935" stroke-width="1"/><line x1="12" y1="3" x2="12" y2="21" stroke="#E53935" stroke-width="1"/><line x1="17" y1="7" x2="17" y2="17" stroke="#E53935" stroke-width="1"/></svg>',
    "molecule": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="4" fill="#0288D1"/><circle cx="6" cy="6" r="3" fill="#0288D1"/><circle cx="18" cy="18" r="3" fill="#0288D1"/><line x1="8" y1="8" x2="10" y2="10" stroke="#0288D1" stroke-width="2"/><line x1="14" y1="14" x2="16" y2="16" stroke="#0288D1" stroke-width="2"/></svg>',
    "brain": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="3" fill="#FF5722"/><circle cx="5" cy="5" r="2" fill="#FF5722"/><circle cx="19" cy="5" r="2" fill="#FF5722"/><circle cx="5" cy="19" r="2" fill="#FF5722"/><circle cx="19" cy="19" r="2" fill="#FF5722"/><line x1="6.5" y1="6.5" x2="10.5" y2="10.5" stroke="#FF5722" stroke-width="1.5"/><line x1="17.5" y1="6.5" x2="13.5" y2="10.5" stroke="#FF5722" stroke-width="1.5"/><line x1="6.5" y1="17.5" x2="10.5" y2="13.5" stroke="#FF5722" stroke-width="1.5"/><line x1="17.5" y1="17.5" x2="13.5" y2="13.5" stroke="#FF5722" stroke-width="1.5"/></svg>',
    "code": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8 9l-4 3 4 3M16 9l4 3-4 3M13 5l-2 14" stroke="#78909C" stroke-width="2" stroke-linecap="round"/></svg>',
    "generic": '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="var(--leaf)" stroke-width="1.5"/><circle cx="12" cy="12" r="3" stroke="var(--leaf)" stroke-width="1.5"/></svg>'
}

def get_fallback_svg(name):
    name_lower = name.lower()
    
    # AWS/Cloud
    if "aws" in name_lower or "amazon" in name_lower or "cloud" in name_lower:
        return fallbacks["aws"]
    # Google Cloud
    if "google" in name_lower or "gcp" in name_lower:
        return fallbacks["gcp"]
    # HPC/Cluster
    if "hpc" in name_lower or "cluster" in name_lower or "linux" in name_lower:
        return fallbacks["hpc"]
    # Chart/Quantification tools
    if any(k in name_lower for k in ["deseq", "edger", "limma", "salmon", "htseq", "cufflinks", "stringtie", "cbioportal", "tcga", "cnvkit", "freely", "exomedepth", "diffbind", "deeptools", "methylkit", "quantification", "expression"]):
        return fallbacks["chart"]
    # Microbiome/Metagenomics
    if any(k in name_lower for k in ["qiime", "kraken", "dada", "mothur", "metaphlan", "picrust", "bracken", "humann", "spades", "megahit", "usearch", "vsearch"]):
        return fallbacks["bacteria"]
    # Network/Pathway
    if any(k in name_lower for k in ["pathway", "network", "cytoscape", "string", "reactome", "kegg", "ontology", "go", "biocarta", "kegg", "genemania", "liana", "cellchat", "cellphonedb", "nichenet"]):
        return fallbacks["network"]
    # DNA/Genomics/Methylation
    if any(k in name_lower for k in ["dna", "rna", "methyl", "chip", "atac", "bismark", "homer", "macs", "meme", "jaspar", "motif", "variant", "vep", "clinvar", "dbsnp", "hgmd", "omim", "oncokb", "genomics"]):
        return fallbacks["dna"]
    # PyMOL/Molecular Modeling
    if any(k in name_lower for k in ["pymol", "vmd", "chimera", "bio3d", "modeller", "autodock", "gromacs", "amber", "openmm", "docking", "simulation", "charmm", "cpptraj", "mdanalysis"]):
        return fallbacks["molecule"]
    # Machine Learning / AI
    if any(k in name_lower for k in ["pytorch", "tensorflow", "keras", "machine", "learning", "ai", "deepchem", "xgboost", "scikit", "model", "adversarial", "gan", "vae"]):
        return fallbacks["brain"]
    # Code languages
    if name_lower in ["r", "python", "perl", "bash", "linux", "c++", "programming"]:
        return fallbacks["code"]
        
    return fallbacks["generic"]

# Regex to find: <div class="rasa-tool"><span class="rasa-tool__mono">XX</span><span class="rasa-tool__name">Tool Name</span></div>
# Let's replace the inner monogram
tool_replace_pattern = re.compile(
    r'(<div\s+class="rasa-tool"\s*>\s*<span\s+class="rasa-tool__mono"\s*>)(.*?)(</span>\s*<span\s+class="rasa-tool__name"\s*>(.*?)</span>\s*</div>)',
    re.DOTALL | re.IGNORECASE
)

def replace_callback(match):
    prefix = match.group(1)
    monogram = match.group(2)
    suffix = match.group(3)
    tool_name = match.group(4).strip()
    
    # Try to find SVG
    svg = tool_svgs.get(tool_name)
    if not svg:
        svg = get_fallback_svg(tool_name)
        
    return f'{prefix}{svg}{suffix}'

for file_name in target_files:
    file_path = os.path.join(workspace_dir, file_name)
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_content = tool_replace_pattern.sub(replace_callback, content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated tool SVGs in {file_name}")
    else:
        print(f"No changes in {file_name}")

print("Tool SVG updates completed!")
