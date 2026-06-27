import os
import re

workspace_dir = r"c:\Users\Nilesh\Desktop\RASALSI\RASA Website\Demo\1"

# Define all pages
pages = [
    "services-ngs.html",
    "services-drug-discovery.html",
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

# Premium SVG Logos Dictionary
# Standard dimensions: viewBox="0 0 24 24" fill="none" width="24" height="24"
premium_svgs = {
    # Languages
    "Python": '<svg viewBox="0 0 24 24" width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path d="M11.93 2c-2.73 0-2.56 1.18-2.56 1.18l.01 1.23h2.61c.73 0 1.33.6 1.33 1.33v2.61h1.23s1.18-.17 1.18-2.56c0-2.39-1.08-3.79-3.79-3.79H11.93zm-3.1 3.1c-.37 0-.67.3-.67.67s.3.67.67.67.67-.3.67-.67-.3-.67-.67-.67zm2.56 4.38v2.61c0 .73-.6 1.33-1.33 1.33H6.45s-1.18.17-1.18 2.56c0 2.39 1.08 3.79 3.79 3.79h2.61s2.56.09 2.56-2.56v-1.23h-2.61a1.33 1.33 0 0 1-1.33-1.33v-2.61L11.39 9.48zM14.9 16c.37 0 .67.3.67.67s-.3.67-.67.67a.67.67 0 0 1-.67-.67c0-.37.3-.67.67-.67z" fill="#3776AB"/><path d="M12.07 22c2.73 0 2.56-1.18 2.56-1.18l-.01-1.23h-2.61c-.73 0-1.33-.6-1.33-1.33v-2.61H9.46s-1.18.17-1.18 2.56c0 2.39 1.08 3.79 3.79 3.79h2.61zM15.17 12.52v-2.61c0-.73.6-1.33 1.33-1.33h2.61s1.18-.17 1.18-2.56C20.29 3.63 19.21 2.23 16.5 2.23h-2.61s-2.56-.09-2.56 2.56v1.23h2.61c.73 0 1.33.6 1.33 1.33v2.61l-1.6 2.56z" fill="#FFE082"/></svg>',
    "R": '<svg viewBox="0 0 24 24" width="24" height="24" xmlns="http://www.w3.org/2000/svg"><ellipse cx="12" cy="12" rx="11" ry="8" fill="url(#r-grad)"/><path d="M7.5 15.5V6.5h4c2.2 0 3.5 1 3.5 2.5 0 1.2-.8 2-2 2.3l2.8 4.2h-2.5l-2.4-3.7H9.2v3.7H7.5zm1.7-5.2h2.2c1.2 0 1.8-.4 1.8-1.1s-.6-1-1.8-1H9.2v2.1z" fill="#276CB4"/><defs><linearGradient id="r-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FFFFFF"/><stop offset="100%" stop-color="#E2E8F0"/></linearGradient></defs></svg>',
    
    # Infrastructure & Clouds
    "Docker": '<svg viewBox="0 0 24 24" width="24" height="24" fill="#0db7ed" xmlns="http://www.w3.org/2000/svg"><path d="M13.9 10.6h-2.1v2.1h2.1v-2.1zm2.7 0H14.5v2.1h2.1v-2.1zm-5.4 0H9.1v2.1h2.1v-2.1zm-2.7 0H6.4v2.1h2.1v-2.1zm8.1-2.7h-2.1v2.1h2.1V7.9zm-2.7 0H11.8v2.1h2.1V7.9zm-2.7 0H9.1v2.1h2.1V7.9zm2.7-2.7H11.8v2.1h2.1V5.2zm8.3 7.8c-.5-.4-1.3-.6-1.9-.4-.1-.7-.4-1.4-.9-1.9a7.3 7.3 0 0 0-4.1-2.1c-.2.7-.6 1.3-1.1 1.7-.6-.1-1.1-.1-1.7 0a3.9 3.9 0 0 0-1.1-1.7 7.3 7.3 0 0 0-4.1 2.1c-.5.5-.8 1.2-.9 1.9-.6-.2-1.4 0-1.9.4-.6.5-.8 1.3-.5 2 .7 1.8 2.4 2.9 4.3 2.9h8.2c1.9 0 3.6-1.1 4.3-2.9.3-.7.1-1.5-.5-2z"/></svg>',
    "Singularity": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="10" stroke="url(#sing-grad)" stroke-width="2"/><circle cx="12" cy="12" r="6" stroke="url(#sing-grad)" stroke-width="1.5" stroke-dasharray="2 1"/><circle cx="12" cy="12" r="3" fill="#00E5FF"/><defs><linearGradient id="sing-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#00ACC1"/><stop offset="100%" stop-color="#00E5FF"/></linearGradient></defs></svg>',
    "AWS": '<svg viewBox="0 0 24 24" width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2A10 10 0 0 0 2 12a10 10 0 0 0 10 10 10 10 0 0 0 10-10A10 10 0 0 0 12 2zm4.3 14c-1.8.8-4.2 1-5.8.2-.5-.3-.9-.6-1-.8-.2-.3 0-.5.3-.4.8.4 2.4.6 3.7.3 1.2-.3 2.3-.9 2.5-1.3.2-.3.4-.2.3.1z" fill="#232F3E"/><path d="M6.3 12.8c1 0 2.2-.4 2.8-.9.6-.5 .8-1.2.7-1.8 0-.6-.4-1.1-1-1.3C8.2 8.6 7 8.5 6 8.7c-1 .2-1.8.7-2.2 1.5-.2.4 0 .6.3.5.5-.2 1.4-.4 2-.4.6 0 1 .2 1 .5 0 .3-.3.5-.8.6-1.2.2-2.3.8-2.6 1.7-.2.6 0 1.2.5 1.5.5.3 1.1.2 1.6-.2z" fill="#FF9900"/></svg>',
    "Google Cloud": '<svg viewBox="0 0 24 24" width="24" height="24" xmlns="http://www.w3.org/2000/svg"><path d="M19.35 10.04C18.67 6.59 15.64 4 12 4 9.11 4 6.6 5.64 5.35 8.04 2.34 8.36 0 10.91 0 14c0 3.31 2.69 6 6 6h13c2.76 0 5-2.24 5-5 0-2.64-2.05-4.78-4.65-4.96z" fill="#4285F4"/></svg>',
    
    # ML / AI
    "TensorFlow": '<svg viewBox="0 0 24 24" width="24" height="24" fill="#FF6F00" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L3 7v10l9 5 9-5V7l-9-5zm0 2.3l6.5 3.6V15l-6.5 3.6L5.5 15V7.9L12 4.3z"/></svg>',
    "PyTorch": '<svg viewBox="0 0 24 24" width="24" height="24" fill="#EE4C2C" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 14.5h-2v-5h2v5zm0-7h-2v-2h2v2z"/></svg>',
    
    # Specific Tool Logos (BIOINFORMATICS)
    "Nextflow": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="url(#nf-grad)" stroke-width="2.5"/><circle cx="12" cy="7" r="2" fill="#10B981"/><circle cx="8" cy="15" r="2" fill="#10B981"/><circle cx="16" cy="15" r="2" fill="#10B981"/><line x1="12" y1="9" x2="9" y2="13" stroke="#10B981" stroke-width="1.5"/><line x1="12" y1="9" x2="15" y2="13" stroke="#10B981" stroke-width="1.5"/><line x1="10" y1="15" x2="14" y2="15" stroke="#10B981" stroke-width="1.5"/><defs><linearGradient id="nf-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#10B981"/><stop offset="100%" stop-color="#059669"/></linearGradient></defs></svg>',
    "Snakemake": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z" stroke="#EF4444" stroke-width="1.5" stroke-dasharray="3 1"/><path d="M7 16c0-2.2 1.8-4 4-4h2c2.2 0 4-1.8 4-4s-1.8-4-4-4-4 1.8-4 4" stroke="#EF4444" stroke-width="2.5" stroke-linecap="round"/><circle cx="17" cy="8" r="1.5" fill="#EF4444"/><defs><linearGradient id="snake-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F87171"/><stop offset="100%" stop-color="#DC2626"/></linearGradient></defs></svg>',
    "Seurat": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="6" cy="16" r="2" fill="#F43F5E"/><circle cx="9" cy="18" r="1.5" fill="#F43F5E"/><circle cx="7" cy="12" r="2" fill="#3B82F6"/><circle cx="12" cy="14" r="1.5" fill="#3B82F6"/><circle cx="15" cy="8" r="2.5" fill="#10B981"/><circle cx="18" cy="5" r="2" fill="#10B981"/><circle cx="14" cy="5" r="1.5" fill="#10B981"/><circle cx="19" cy="10" r="1.5" fill="#10B981"/></svg>',
    "Scanpy": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 18c2-4 6-6 10-6s8 4 8 4" stroke="#3776AB" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="6" r="3.5" fill="#FFD43B" stroke="#3776AB" stroke-width="1.2"/><circle cx="6" cy="13" r="2" fill="#3776AB"/><circle cx="18" cy="13" r="2" fill="#3776AB"/></svg>',
    "Bioconductor": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="#87B13F" stroke-width="2" stroke-dasharray="4 2"/><path d="M8 12c0-2.2 1.8-4 4-4s4 1.8 4 4-1.8 4-4 4" stroke="#2D882D" stroke-width="2" stroke-linecap="round"/><circle cx="12" cy="12" r="2" fill="#D32F2F"/></svg>',
    
    # Specific Tool Logos (DRUG DISCOVERY)
    "GROMACS": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="#E91E63" stroke-width="2"/><circle cx="6" cy="12" r="2" fill="#E91E63"/><circle cx="18" cy="12" r="2" fill="#E91E63"/><circle cx="12" cy="6" r="2" fill="#3F51B5"/><circle cx="12" cy="18" r="2" fill="#3F51B5"/><line x1="6" y1="12" x2="18" y2="12" stroke="#64748B" stroke-width="1"/><line x1="12" y1="6" x2="12" y2="18" stroke="#64748B" stroke-width="1"/></svg>',
    "AMBER": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="4.5" fill="#FF5722"/><circle cx="6" cy="7" r="3" fill="#795548"/><circle cx="18" cy="7" r="3" fill="#795548"/><circle cx="12" cy="19" r="3" fill="#795548"/><line x1="12" y1="12" x2="6" y2="7" stroke="#795548" stroke-width="1.8"/><line x1="12" y1="12" x2="18" y2="7" stroke="#795548" stroke-width="1.8"/><line x1="12" y1="12" x2="12" y2="19" stroke="#795548" stroke-width="1.8"/></svg>',
    "AutoDock Vina": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="#4CAF50" stroke-width="2" stroke-dasharray="3 3"/><circle cx="12" cy="12" r="4.5" fill="#4CAF50"/><path d="M6 12h12M12 6v12" stroke="#4CAF50" stroke-width="1.2"/></svg>',
    
    # Tool Categories Fallbacks
    "aws_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 7l10 5 10-5-10-5z" fill="#FF9900"/><path d="M2 17l10 5 10-5M2 12l10 5 10-5" stroke="#FF9900" stroke-width="1.5"/></svg>',
    "gcp_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L3 7v10l9 5 9-5V7l-9-5z" stroke="#4285F4" stroke-width="1.5"/><circle cx="12" cy="12" r="3" fill="#4285F4"/></svg>',
    "hpc_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="3" width="18" height="5" rx="1" fill="#455A64"/><rect x="3" y="10" width="18" height="5" rx="1" fill="#455A64"/><rect x="3" y="17" width="18" height="5" rx="1" fill="#455A64"/><circle cx="6" cy="5.5" r="1" fill="#00E676"/><circle cx="6" cy="12.5" r="1" fill="#00E676"/><circle cx="6" cy="19.5" r="1" fill="#00E676"/></svg>',
    
    # Generic Themed Database Logo
    "db_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 6c0-1.66 3.58-3 8-3s8 1.34 8 3m-16 0v4c0 1.66 3.58 3 8 3s8-1.34 8-3V6m-16 4v4c0 1.66 3.58 3 8 3s8-1.34 8-3v-4m-16 4v4c0 1.66 3.58 3 8 3s8-1.34 8-3v-4" stroke="url(#db-grad)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="db-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#4F46E5"/><stop offset="100%" stop-color="#06B6D4"/></linearGradient></defs></svg>',
    
    # Generic Themed DNA Helix Logo
    "dna_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4.5 10.5c0 0 3.5-7.5 7.5-7.5s7.5 7.5 7.5 7.5m-15 3c0 0 3.5 7.5 7.5 7.5s7.5-7.5 7.5-7.5" stroke="url(#dna-grad)" stroke-width="2" stroke-linecap="round"/><path d="M6 7.5h12M4.5 12h15M6 16.5h12" stroke="url(#dna-grad)" stroke-width="1.5" stroke-linecap="round"/><defs><linearGradient id="dna-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#10B981"/><stop offset="100%" stop-color="#059669"/></linearGradient></defs></svg>',
    
    # Generic Themed Chart/Analytics Logo
    "chart_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M3 3v18h18" stroke="#64748B" stroke-width="2" stroke-linecap="round"/><path d="M7 14l4-4 5 5 4-7" stroke="url(#chart-grad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="7" cy="14" r="2" fill="#3B82F6"/><circle cx="11" cy="10" r="2" fill="#3B82F6"/><circle cx="16" cy="15" r="2" fill="#3B82F6"/><circle cx="20" cy="7" r="2" fill="#3B82F6"/><defs><linearGradient id="chart-grad" x1="0" y1="1" x2="1" y2="0"><stop offset="0%" stop-color="#3B82F6"/><stop offset="100%" stop-color="#8B5CF6"/></linearGradient></defs></svg>',
    
    # Generic Themed Network/Pathway Logo
    "network_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="5" r="3" fill="url(#net-g1)"/><circle cx="6" cy="14" r="3" fill="url(#net-g2)"/><circle cx="18" cy="14" r="3" fill="url(#net-g2)"/><circle cx="12" cy="20" r="2" fill="url(#net-g3)"/><line x1="12" y1="8" x2="6.8" y2="11.5" stroke="#6366F1" stroke-width="1.5"/><line x1="12" y1="8" x2="17.2" y2="11.5" stroke="#6366F1" stroke-width="1.5"/><line x1="6.8" y1="15.8" x2="11.2" y2="18.8" stroke="#6366F1" stroke-width="1.5"/><line x1="17.2" y1="15.8" x2="12.8" y2="18.8" stroke="#6366F1" stroke-width="1.5"/><line x1="6" y1="14" x2="18" y2="14" stroke="#4F46E5" stroke-width="1" stroke-dasharray="2 2"/><defs><linearGradient id="net-g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#818CF8"/><stop offset="100%" stop-color="#4F46E5"/></linearGradient><linearGradient id="net-g2" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#34D399"/><stop offset="100%" stop-color="#059669"/></linearGradient><linearGradient id="net-g3" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F59E0B"/><stop offset="100%" stop-color="#D97706"/></linearGradient></defs></svg>',
    
    # Generic Themed Molecular Structure Logo
    "molecule_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" fill="url(#mol-grad1)" stroke="#1E293B" stroke-width="1"/><circle cx="5" cy="6" r="3" fill="url(#mol-grad2)" stroke="#1E293B" stroke-width="1"/><circle cx="19" cy="6" r="3" fill="url(#mol-grad2)" stroke="#1E293B" stroke-width="1"/><circle cx="19" cy="18" r="3.5" fill="url(#mol-grad3)" stroke="#1E293B" stroke-width="1"/><line x1="7.4" y1="7.8" x2="9.6" y2="9.6" stroke="#475569" stroke-width="2.5"/><line x1="16.6" y1="7.8" x2="14.4" y2="9.6" stroke="#475569" stroke-width="2.5"/><line x1="15.5" y1="15.5" x2="17" y2="17" stroke="#475569" stroke-width="2.5"/><defs><linearGradient id="mol-grad1" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#FF8A65"/><stop offset="100%" stop-color="#E64A19"/></linearGradient><linearGradient id="mol-grad2" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#4FC3F7"/><stop offset="100%" stop-color="#0288D1"/></linearGradient><linearGradient id="mol-grad3" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#AED581"/><stop offset="100%" stop-color="#689F38"/></linearGradient></defs></svg>',
    
    # Generic Themed AI/ML Node Brain Logo
    "brain_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z" stroke="url(#ai-grad)" stroke-width="1.8" stroke-dasharray="2 1"/><circle cx="12" cy="12" r="3.5" fill="#EF4444"/><circle cx="6" cy="8" r="2" fill="#3B82F6"/><circle cx="18" cy="8" r="2" fill="#10B981"/><circle cx="6" cy="16" r="2" fill="#F59E0B"/><circle cx="18" cy="16" r="2" fill="#8B5CF6"/><line x1="7.5" y1="9" x2="10.5" y2="11" stroke="#94A3B8" stroke-width="1.2"/><line x1="16.5" y1="9" x2="13.5" y2="11" stroke="#94A3B8" stroke-width="1.2"/><line x1="7.5" y1="15" x2="10.5" y2="13" stroke="#94A3B8" stroke-width="1.2"/><line x1="16.5" y1="15" x2="13.5" y2="13" stroke="#94A3B8" stroke-width="1.2"/><defs><linearGradient id="ai-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#F43F5E"/><stop offset="100%" stop-color="#EC4899"/></linearGradient></defs></svg>',
    
    # Generic Themed Microbiome Bacteria Logo
    "bacteria_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="5" y="7" width="14" height="10" rx="5" stroke="url(#bac-grad)" stroke-width="2" stroke-linecap="round"/><path d="M19 12h3M2 12h3M7 10h.01M11 12h.01M15 14h.01M10 8h2M12 16h2" stroke="url(#bac-grad)" stroke-width="1.8" stroke-linecap="round"/><defs><linearGradient id="bac-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0D9488"/><stop offset="100%" stop-color="#0F766E"/></linearGradient></defs></svg>',
    
    # Generic Themed Code Terminal Logo
    "code_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="4" width="18" height="16" rx="2" stroke="url(#code-grad)" stroke-width="1.8"/><path d="M7 9l3 3-3 3m5 0h5" stroke="url(#code-grad)" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><defs><linearGradient id="code-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#64748B"/><stop offset="100%" stop-color="#334155"/></linearGradient></defs></svg>',
    
    # General Default Generic Logo
    "default_generic": '<svg viewBox="0 0 24 24" width="24" height="24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="url(#gen-grad)" stroke-width="1.8" stroke-dasharray="3 1"/><circle cx="12" cy="12" r="3" fill="url(#gen-grad)"/><defs><linearGradient id="gen-grad" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#10B981"/><stop offset="100%" stop-color="#3B82F6"/></linearGradient></defs></svg>'
}

def get_premium_svg(tool_name):
    name_clean = tool_name.strip()
    
    # Exact check (case-insensitive)
    for key, value in premium_svgs.items():
        if key.lower() == name_clean.lower():
            return value
        
    name_lower = name_clean.lower()
    
    # AWS/Cloud
    if "aws" in name_lower or "amazon" in name_lower or "cloud" in name_lower:
        return premium_svgs["aws_generic"]
    # Google Cloud
    if "google" in name_lower or "gcp" in name_lower:
        return premium_svgs["gcp_generic"]
    # HPC/Cluster
    if "hpc" in name_lower or "cluster" in name_lower or "linux" in name_lower:
        return premium_svgs["hpc_generic"]
    # Chart/Quantification tools
    if any(k in name_lower for k in ["deseq", "edger", "limma", "salmon", "htseq", "cufflinks", "stringtie", "cbioportal", "tcga", "cnvkit", "freely", "exomedepth", "diffbind", "deeptools", "methylkit", "quantification", "expression", "fastqc", "multiqc", "multi-qc", "fast-qc"]):
        return premium_svgs["chart_generic"]
    # Microbiome/Metagenomics
    if any(k in name_lower for k in ["qiime", "kraken", "dada", "mothur", "metaphlan", "picrust", "bracken", "humann", "spades", "megahit", "usearch", "vsearch"]):
        return premium_svgs["bacteria_generic"]
    # Network/Pathway
    if any(k in name_lower for k in ["pathway", "network", "cytoscape", "string", "reactome", "kegg", "ontology", "go", "biocarta", "genemania", "liana", "cellchat", "cellphonedb", "nichenet"]):
        return premium_svgs["network_generic"]
    # DNA/Genomics/Methylation
    if any(k in name_lower for k in ["dna", "rna", "methyl", "chip", "atac", "bismark", "homer", "macs", "meme", "jaspar", "motif", "variant", "vep", "clinvar", "dbsnp", "hgmd", "omim", "oncokb", "genomics", "bwa", "gatk", "deepvariant", "bcftools", "annovar", "star", "hisat"]):
        return premium_svgs["dna_generic"]
    # PyMOL/Molecular Modeling/Docking/Dynamics
    if any(k in name_lower for k in ["pymol", "vmd", "chimera", "bio3d", "modeller", "autodock", "gromacs", "amber", "openmm", "docking", "simulation", "charmm", "cpptraj", "mdanalysis", "vina", "smina", "quickvina", "cbdock", "cb-dock"]):
        return premium_svgs["molecule_generic"]
    # Machine Learning / AI
    if any(k in name_lower for k in ["pytorch", "tensorflow", "keras", "machine", "learning", "ai", "deepchem", "xgboost", "scikit", "model", "adversarial", "gan", "vae", "neural", "deep"]):
        return premium_svgs["brain_generic"]
    # Code languages
    if name_lower in ["r", "python", "perl", "bash", "linux", "c++", "programming"]:
        return premium_svgs["code_generic"]
        
    return premium_svgs["default_generic"]

# Regex to find tool boxes in HTML files and replace the monogram/inner SVG
tool_replace_pattern = re.compile(
    r'(<div\s+class="rasa-tool"\s*>\s*<span\s+class="rasa-tool__mono"\s*>)(.*?)(</span>\s*<span\s+class="rasa-tool__name"\s*>(.*?)</span>\s*</div>)',
    re.DOTALL | re.IGNORECASE
)

def replace_callback(match):
    prefix = match.group(1)
    inner_mono = match.group(2)
    suffix = match.group(3)
    tool_name = match.group(4).strip()
    
    svg = get_premium_svg(tool_name)
    return f'{prefix}{svg}{suffix}'

# Run replacement over all HTML files
for page in pages:
    file_path = os.path.join(workspace_dir, page)
    if not os.path.exists(file_path):
        continue
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    new_content = tool_replace_pattern.sub(replace_callback, content)
    
    if new_content != content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated premium tool logos in {page}")
    else:
        print(f"No changes in {page}")

print("Premium tool logo updates completed!")
