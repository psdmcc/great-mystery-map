#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mysterium_analytics.py
Advanced Philological Analytics & Geo-Spatial Vector Mapping Engine.
Computes degree centrality scores and injects ToposText geographical coordinates.
"""
import csv
import os
import networkx as nx

INPUT_FILE = "mysterium_toxicology_matrix.csv"
OUTPUT_ANALYTICS = "mysterium_centrality_rankings.csv"
OUTPUT_GEO = "mysterium_geospatial_vectors.csv"

# Pre-compiled authoritative ToposText coordinates matching your corpus
geo_directory = {
    "galen": {"site": "Rome / Pergamum", "lat": 41.9028, "lon": 12.4964},
    "hippocrates": {"site": "Cos Asclepieion", "lat": 36.8914, "lon": 27.2872},
    "euripides": {"site": "Athens (Theater of Dionysus)", "lat": 37.9715, "lon": 23.7275},
    "plato": {"site": "Athens (Academy / State Prison)", "lat": 37.9715, "lon": 23.7275},
    "sophocles": {"site": "Athens (Colonus)", "lat": 37.9715, "lon": 23.7275},
    "aeschylus": {"site": "Athens / Sicily", "lat": 37.0755, "lon": 15.2866},
    "theophrastus": {"site": "Eresos / Athens", "lat": 39.1683, "lon": 25.9317},
    "gospel": {"site": "Jerusalem / Rome", "lat": 31.7683, "lon": 35.2137},
    "cyril": {"site": "Alexandria", "lat": 31.2001, "lon": 29.9187},
    "catenae": {"site": "Alexandria / Byzantium", "lat": 41.0082, "lon": 28.9784},
    "chronicon": {"site": "Constantinople", "lat": 41.0082, "lon": 28.9784}
}

def main():
    print("="*60)
    print("MYSTERIUM ANALYTICS & GEOSPATIAL VECTOR MODULE ONLINE")
    print("="*60)
    
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: Cannot locate source file '{INPUT_FILE}'.")
        return

    G = nx.Graph()
    rows_data = []

    with open(INPUT_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            work = row.get("Work_Title", "Unknown").replace("\n", " ").strip()
            work = " ".join(work.split())
            themes = row.get("Overlapping_Themes", "")
            keywords = row.get("Greek_Keywords", "")
            snippet = row.get("Greek_Context_Snippet", "")
            url = row.get("Perseus_Web_URL", "")
            
            rows_data.append({"work": work, "themes": themes, "keywords": keywords, "snippet": snippet, "url": url})
            
            G.add_node(work, type="source")
            theme_list = [t.strip() for t in themes.split("|") if t.strip()]
            for t in theme_list:
                G.add_node(t, type="concept")
                G.add_edge(work, t)

    # 1. Compute Degree Centrality Matrix
    degrees = dict(G.degree())
    total_nodes = len(G.nodes())
    centrality_rankings = []
    
    for node in G.nodes():
        if G.nodes[node].get("type") == "source":
            deg = degrees[node]
            score = deg / (total_nodes - 1) if total_nodes > 1 else 0
            centrality_rankings.append([node, deg, round(score, 3)])
            
    centrality_rankings.sort(key=lambda x: x[1], reverse=True)

    with open(OUTPUT_ANALYTICS, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Work_Title", "Connection_Degree", "Degree_Centrality_Score"])
        writer.writerows(centrality_rankings)
    print(f"[+] Centrality matrix compiled to '{OUTPUT_ANALYTICS}'.")

    # 2. Extract Geo-Spatial Mapping Vectors
    geo_rows = []
    for r in rows_data:
        work_lower = r["work"].lower()
        site_name, lat, lon = "Unknown Ancient Site", 0.0, 0.0
        
        for key, geo in geo_directory.items():
            if key in work_lower:
                site_name = geo["site"]
                lat = geo["lat"]
                lon = geo["lon"]
                break
                
        geo_rows.append([r["work"], site_name, lat, lon, r["themes"], r["keywords"], r["snippet"], r["url"]])

    with open(OUTPUT_GEO, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Work_Title", "ToposText_Ancient_Site", "Latitude_Vector", "Longitude_Vector", "Overlapping_Themes", "Greek_Keywords", "Greek_Context_Snippet", "Perseus_Web_URL"])
        writer.writerows(geo_rows)
    print(f"[+] Geo-spatial vectors mapped cleanly to '{OUTPUT_GEO}'.")
    print("="*60)

if __name__ == "__main__":
    main()
