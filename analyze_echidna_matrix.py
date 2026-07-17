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
