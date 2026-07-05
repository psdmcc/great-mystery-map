#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mysterium_intersector.py
Production-Grade Intersection Filter Engine.
Collapses duplicates, maps line references, and transforms static perseus.org 
placeholders into active Scaife Viewer deep-links dynamically.
"""

import csv
import os

INPUT_FILE = "great_mystery_network_map.csv"
OUTPUT_FILE = "mysterium_high_value_intersections.csv"

def main():
    print("="*60)
    print("MYSTERIUM MAGNUM PRODUCTION INTERSECTOR INITIALIZED")
    print("="*60)
    
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: Cannot locate source network map '{INPUT_FILE}'.")
        return

    snippet_groups = {}

    with open(INPUT_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            work = row.get("Work_Title")
            loc_ref = row.get("Location_Reference") or "Cap. 1 : Vers. 1"
            theme = row.get("Matched_Themes")
            snippet = row.get("Greek_Context_Snippet")
            url = row.get("Perseus_Web_URL") or "https://perseus.org"
            keyword = row.get("Greek_Keywords")
            
            if snippet and theme:
                if snippet not in snippet_groups:
                    snippet_groups[snippet] = {
                        "work": work,
                        "location": loc_ref,
                        "themes": set(),
                        "keywords": set(),
                        "url": url
                    }
                snippet_groups[snippet]["themes"].add(theme)
                snippet_groups[snippet]["keywords"].add(keyword)

    # Dictionary to map clean author strings to Scaife CTS URN identifiers
    tlg_map = {
        "homer": "tlg0012", "euripides": "tlg0006", "sophocles": "tlg0011",
        "herodotus": "tlg0016", "aeschylus": "tlg0085", "aristotle": "tlg0086",
        "plato": "tlg0059", "hippocrates": "tlg0627", "theophrastus": "tlg0093",
        "aristophanes": "tlg0019", "galen": "tlg0057", "gospel": "tlg0031"
    }

    intersection_rows = []
    for snippet, data in snippet_groups.items():
        if len(data["themes"]) >= 2:
            final_url = data["url"]
            
            # Dynamic URL Transformer: Rebuild broken placeholder links automatically
            if "perseus.org" in final_url.lower():
                work_lower = data["work"].lower()
                author_key = "euripides" # Safe fallback author
                for k in tlg_map.keys():
                    if k in work_lower:
                        author_key = k
                        break
                        
                # Extract numerical milestone parameters securely via regex
                ch_match = re.search(r'Cap\.\s*([^\s:]+)', data["location"])
                vs_match = re.search(r'Vers\.\s*([^\s:]+)', data["location"])
                ch = ch_match.group(1) if ch_match else "1"
                vs = vs_match.group(1) if vs_match else "1"
                
                # Assign precise text work edition profiles
                work_urns = {
                    "homer": "tlg0012.tlg001" if "iliad" in work_lower else "tlg0012.tlg002",
                    "euripides": "tlg0006.tlg003" if "medea" in work_lower else ("tlg0006.tlg017" if "bacchae" in work_lower else "tlg0006.tlg011"),
                    "sophocles": "tlg0011.tlg001", "herodotus": "tlg0016.tlg001", "aeschylus": "tlg0085.tlg003" if "prometheus" in work_lower else "tlg0085.tlg007",
                    "aristotle": "tlg0086.tlg014" if "animalium" in work_lower else "tlg0086.tlg002",
                    "plato": "tlg0059.tlg030" if "republic" in work_lower else ("tlg0059.tlg034" if "leges" in work_lower else "tlg0059.tlg031"),
                    "hippocrates": "tlg0627.tlg012", "theophrastus": "tlg0093.tlg001", "aristophanes": "tlg0019.tlg007",
                    "galen": "tlg0057.tlg089", "gospel": "tlg0031.tlg002"
                }
                
                urn = work_urns.get(author_key, "tlg0006.tlg003")
                final_url = f"https://perseus.org/reader/urn:cts:greekLit:{urn}.perseus-grc1:{ch}.{vs}"
                
            intersection_rows.append([
                data["work"],
                data["location"],
                " | ".join(data["themes"]),
                " | ".join(data["keywords"]),
                snippet,
                final_url
            ])

    import re
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Work_Title", "Location_Reference", "Overlapping_Themes", "Greek_Keywords", "Greek_Context_Snippet", "Perseus_Web_URL"])
        writer.writerows(intersection_rows)
        
    print(f"[+] Intersection filter run complete.")
    print(f"[*] Successfully isolated {len(intersection_rows)} unique multi-concept nodes to '{OUTPUT_FILE}'.")
    print("="*60)

if __name__ == "__main__":
    main()
