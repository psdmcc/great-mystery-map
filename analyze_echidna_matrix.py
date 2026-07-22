import os
import re
import pandas as pd

def run_expanded_matrix_analysis(raw_texts_dir="raw_texts"):
    """
    Sweeps the 2,491 corpus assets to audit the structural proximity
    between the Echidna Priestess, Pharmako-Mantis variables, and 
    the Hippocratic non-lethality boundary.
    """
    if not os.path.exists(raw_texts_dir):
        print(f"[-] Operational Error: Subdirectory './{raw_texts_dir}' not found.")
        return

    # Expanded morphological regex patterns capturing the full 6-part thesis matrix
    target_patterns = {
        'Echidna_Priestess': re.compile(r"\b(ἐχιδν[-]{0,2}|εχιδν[-]{0,2}|echidn)", re.IGNORECASE | re.UNICODE),
        'Pharmako_Mantis': re.compile(r"\b(φαρμακομαντ[-]{0,2}|φαρμακο-μαντ[-]{0,2}|pharmakomant)", re.IGNORECASE | re.UNICODE),
        'Hippocratic_Thanasimon': re.compile(r"\b(θανασιμ[-]{0,2}|thanasim)", re.IGNORECASE | re.UNICODE),
        'Soterion_Pharmakon': re.compile(r"\b(σωτηρ[-]{0,2}|σωτερ[-]{0,2}|φαρμακ[-]{0,2})", re.IGNORECASE | re.UNICODE),
        'Evangelion_Efficacy': re.compile(r"\b(εὐαγγελ[-]{0,2}|ευαγγελ[-]{0,2})", re.IGNORECASE | re.UNICODE),
        'Christos_Compound': re.compile(r"\b(χριστ[-]{0,2}|χρισ[-]{0,2}|χρισμ[-]{0,2}|χριω|χριο)", re.IGNORECASE | re.UNICODE)
        "purple_dye": re.compile(r"\bπορφυρ(?:α|ᾱ|ας|ᾳ|αν|ων|αις|ες|ο|οῦ|ᾶς|οῦν|οῖ)\w*\b", re.IGNORECASE),
        "drakaina": re.compile(r"\bδρακαιν(?:α|ης|ῃ|αν|αι|ων|αις)\b", re.IGNORECASE),
        "gypsum": re.compile(r"\bγυψ(?:ος|ου|ῳ|ον|ε|ων|οις|ους)\b", re.IGNORECASE),
        "theriake_vessel": re.compile(r"\bθηριακ\w*\b", re.IGNORECASE),
        "galene_stabilization": re.compile(r"\bγαλην(?:η|ης|ῃ|αν|αι|ων|αις)\b", re.IGNORECASE),
        "dialysis_neutralization": re.compile(r"\bδιαλυ(?:ω|εις|ει|ομεν|ετε|ουσι|ειν|ης|η|ον)\b", re.IGNORECASE),
        "somatic_ingestion": re.compile(r"\b(αἱμα|σαρκ|ἑψειν|πινειν)\w*\b", re.IGNORECASE),
        "heresiological_synthesis": re.compile(r"\b(μανιχαι|συντιθε|αθανασι|αμβροσι)\w*\b", re.IGNORECASE),
        "byzantine_translatio": re.compile(r"\b(εχιδνολογ|σαρκ|ἑρπιστικ|σωτηρι)\w*\b", re.IGNORECASE),
        "generic_serpent": re.compile(r"\bοφι(?:ς|ος|ῳ|ον|ε|ων|οις|ους)\b", re.IGNORECASE),
        "dipsas_dehydration": re.compile(r"\bδιψα\w*\b", re.IGNORECASE),
        "synchrisma_ointment": re.compile(r"\bσυγχρισμ\w*\b", re.IGNORECASE),
        "draconic_agent": re.compile(r"\bδρακοντ(?:ος|ῳ|α|ες|ων|οις|ους)\b", re.IGNORECASE),
        "potable_vehicle": re.compile(r"\b(ποθεισ|πινω|οινω)\w*\b", re.IGNORECASE),
        "corporate_tech_transfer": re.compile(r"\b(χριομεν|σαρκων|σκευασια|αντιδοτ)\w*\b", re.IGNORECASE),
        "gnostic_pushback": re.compile(r"\b(ληστ|ληστρικ|μανιχ|ναγ[-_]χαμμ)\w*\b", re.IGNORECASE),
        "scythian_ballistics": re.compile(r"\b(σκυθικ|οϊστου|οιστο)\w*\b", re.IGNORECASE),
        "ballistic_chrisma": re.compile(r"\b(χρισμα_βελ|χριουσιν|αβαριδ)\w*\b", re.IGNORECASE),
        "theriake_vessel": re.compile(r"\bθηριακ\w*\b", re.IGNORECASE),
        "galene_stabilization": re.compile(r"\bγαλην(?:η|ης|ῃ|αν|αι|ων|αις)\b", re.IGNORECASE),
        "dialysis_neutralization": re.compile(r"\bδιαλυ(?:ω|εις|ει|ομεν|ετε|ουσι|ειν|ης|η|ον)\b", re.IGNORECASE),
        "somatic_ingestion": re.compile(r"\b(αἱμα|σαρκ|ἑψειν|πινειν)\w*\b", re.IGNORECASE),
        "heresiological_synthesis": re.compile(r"\b(μανιχαι|συντιθε|αθανασι|αμβροσι)\w*\b", re.IGNORECASE),
        "byzantine_translatio": re.compile(r"\b(εχιδνολογ|σαρκ|ἑρπιστικ|σωτηρι)\w*\b", re.IGNORECASE),
        "generic_serpent": re.compile(r"\bοφι(?:ς|ος|ῳ|ον|ε|ων|οις|ους)\b", re.IGNORECASE),
        "dipsas_dehydration": re.compile(r"\bδιψα\w*\b", re.IGNORECASE),
        "synchrisma_ointment": re.compile(r"\bσυγχρισμ\w*\b", re.IGNORECASE),
        "draconic_agent": re.compile(r"\bδρακοντ(?:ος|ῳ|α|ες|ων|οις|ους)\b", re.IGNORECASE),
        "potable_vehicle": re.compile(r"\b(ποθεισ|πινω|οινω)\w*\b", re.IGNORECASE),
        "corporate_tech_transfer": re.compile(r"\b(χριομεν|σαρκων|σκευασια|αντιδοτ)\w*\b", re.IGNORECASE),
        "gnostic_pushback": re.compile(r"\b(ληστ|ληστρικ|μανιχ|ναγ[-_]χαμμ)\w*\b", re.IGNORECASE),
        "scythian_ballistics": re.compile(r"\b(σκυθικ|οϊστου|οιστο)\w*\b", re.IGNORECASE),
        "ballistic_chrisma": re.compile(r"\b(χρισμα_βελ|χριουσιν|αβαριδ)\w*\b", re.IGNORECASE)
}

    print(f"[*] Sweeping 2,491 assets for the Expanded Pharmako-Mantis Matrix...")
    
    extracted_records = []
    file_list = [f for f in os.listdir(raw_texts_dir) if os.path.isfile(os.path.join(raw_texts_dir, f))]
    
    for file_name in file_list:
        file_path = os.path.join(raw_texts_dir, file_name)
        if file_name.startswith('.') or file_name.endswith(('.pdf', '.csv')):
            continue
            
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception:
            continue

        # Segment document content into clear sentence units
        sentences = re.split(r'(?<=[.!?])\s+', content)
        
        for sentence in sentences:
            clean_sentence = sentence.strip().replace('\n', ' ')
            if len(clean_sentence) < 15:
                continue
                
            # Scan active string segment for overlapping term matrices
            matched_nodes = []
            for label, pattern in target_patterns.items():
                if pattern.search(clean_sentence):
                    matched_nodes.append(label)
            
            # Capture proximity intersections where at least TWO elements from the matrix collide
            if len(matched_nodes) >= 2:
                extracted_records.append({
                    'Source_Document': file_name,
                    'Co_occurring_Nodes': ", ".join(matched_nodes),
                    'Contextual_Evidence_Snippet': clean_sentence
                })

    if extracted_records:
        output_file = "echidna_salvation_matrix.csv"
        df = pd.DataFrame(extracted_records)
        df.to_csv(output_file, index=False)
        print("-" * 75)
        print(f"[+] Success: Harvested {len(df)} concrete text intersections across the expanded matrix!")
        print(f"[+] Empirical dataset ledger successfully rewritten at:\n    {os.path.abspath(output_file)}")
        print("-" * 75)
    else:
        print("[-] Target Extraction Alert: No overlapping strings recorded. Verify patterns.")

if __name__ == "__main__":
    run_expanded_matrix_analysis()
