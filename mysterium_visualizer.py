#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mysterium_visualizer.py
Upgraded All-Label Production Network Graph Visualizer Engine.
Displays 100% of manuscript titles with translucent backdrop shields to prevent overlapping text.
"""
import csv
import os
import networkx as nx
import matplotlib.pyplot as plt
import re

INPUT_FILE = "mysterium_toxicology_matrix.csv"

def main():
    print("="*60)
    print("MYSTERIUM HIGH-FIDELITY NETWORK GRAPH GENERATOR ONLINE")
    print("="*60)
    
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: Cannot locate source data file '{INPUT_FILE}'.")
        return

    G = nx.Graph()

    with open(INPUT_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            work = row.get("Work_Title", "Unknown Work")
            themes_str = row.get("Overlapping_Themes", "")
            
            if work and themes_str:
                work_clean = work.replace("\\n", " ").strip()
                work_clean = re.sub(r'\s+', ' ', work_clean)
                
                G.add_node(work_clean, type="source")
                themes = [t.strip() for t in themes_str.split("|") if t.strip()]
                for theme in themes:
                    G.add_node(theme, type="concept")
                    G.add_edge(work_clean, theme)

    if len(G.nodes()) == 0:
        print("[!] Network Graph data pool is empty. Re-run your processing filters.")
        return

    plt.figure(figsize=(15, 10), dpi=150)
    
    # Balanced spring spacing constant to handle all titles cleanly
    pos = nx.spring_layout(G, k=1.4, iterations=60, seed=42)
    
    degrees = dict(G.degree())
    
    node_colors = []
    node_sizes = []
    labels_to_draw = {}
    
    for node, data in G.nodes(data=True):
        deg = degrees[node]
        if G.nodes[node].get("type") == "source":
            node_colors.append("#e53935") # Crimson Red for text works
            node_sizes.append(120 + (deg * 50)) 
            labels_to_draw[node] = node # Verified: Restored 100% of text labels
        else:
            node_colors.append("#1e88e5") # High-visibility azure blue for keywords
            node_sizes.append(350)
            labels_to_draw[node] = node

    # Draw nodes and structural lines cleanly
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.9, edgecolors="#37474f", linewidths=1.0)
    nx.draw_networkx_edges(G, pos, width=0.6, edge_color="#b0bec5", alpha=0.4)
    
    # FIX: Add a white translucent backdrop shield bounding box behind text labels
    nx.draw_networkx_labels(
        G, pos, labels=labels_to_draw, 
        font_size=6.0, 
        font_weight="bold", 
        font_family="sans-serif",
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.7)
    )
    
    plt.title("Mysterium Magnum: High-Density Cross-Thematic Overlap Graph (Complete Ledger)", fontsize=14, pad=20, weight="bold")
    plt.axis("off")
    plt.tight_layout()
    
    output_img = "mysterium_network_map.png"
    plt.savefig(output_img, bbox_inches='tight')
    print(f"[+] Success! Structural layout chart visualization saved to '{output_img}'.")
    plt.show()

if __name__ == "__main__":
    main()
