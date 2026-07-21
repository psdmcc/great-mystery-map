# The Medicalization of the Soul: A Computational Corpus and Network Analysis of Lexical Translatio in Late Antique Scientia

This repository contains the complete programmatic compute infrastructure, analytical pipeline dependencies, regular expression scripts, and localized co-occurrence matrix sheets backing the research manuscript *"The Medicalization of the Soul"*. 

## 📊 Core Corpus Specifications
* **Total Textual Assets**: 2,491 distinct discrete documents.
* **Lemma Nodes Isolated**: 33 unique technical profiles.
* **Undirected Edge Weights**: 218 verified structural connections.
* **Concrete Text Intersections**: 1,921 automated sliding-window hits ($W = 150$).
* **Network Graph Peak Bottleneck**: `ἰός` (Venom/Toxin; Betweenness Centrality: 0.3557).

## 🗂️ Repository Architecture
├── generate_web_map.py               # Principal PyVis force-directed network layout engine├── manuscript.tex                    # LaTeX source text core file (publication-ready)├── manuscript.pdf                    # Finalizedypeset double-pass layout document├── master_word_list.csv              # Full token dictionary mapping the 42 regex roots├── mysterium_centrality_rankings.csv # Computed metrics tracking Degree, Betweenness, and PageRank├── mysterium_graph.png               # High-density visualization of the cross-thematic graph├── alexandria_node.csv               # Localized text intersection sheets mapping patristic data├── byzantium_node.csv                # Localized historiographical text matrix layers├── cos_node.csv                      # Classical Hippocratic medical corpus dataset strings└── rome_node.csv                     # Late Roman social history data nodes
## 🚀 Execution & Replication Pipeline

### 1. Environment Initialization
Ensure you are operating within an active virtual environment running Python 3.11:
```bash
python3 -m venv venv
source venv/bin/activate
pip install pandas networkx pyvis
```

### 2. Network Map Generation
Execute the main visualization script to compute Brandes’ algorithmic logic and compile the interactive network topology:
```bash
python3 generate_web_map.py
```
*Note: The physics envelope uses a Javascript-backed Barnes-Hut force-directed simulation programmatically locked to a gravitational spring constant of `-2000` to compress hyper-dense hubs (`katharsis, christos`) while isolating volatile ecstatic registers (`oistros, lyssa`) on the canvas fringe.*

### 3. LaTeX Document Compilation
To compile the source manuscript directly from your machine terminal without hitting interactive freezes, pass the nonstop batch flag through your compilation loop:
```bash
rm -f manuscript.aux manuscript.log
pdflatex -interaction=nonstopmode manuscript.tex
```

## 📜 Public Deployment & Availability
* **Live Repository Tree**: [psdmcc/great-mystery-map](https://github.com)
* **Interactive Visualization Client**: Served via Vercel at [https://vercel.app](https://vercel.app)

## 🏛️ Citation Mapping
If you utilize this pipeline, data matrices, or text-mining datasets in your research, please cite the core manuscript:
```bibtex
@article{mccartney2026medicalization,
  author  = {McCartney, Patrick S.D.},
  title   = {The Medicalization of the Soul: A Computational Corpus and Network Analysis of Lexical Translatio and Cross-Thematic Overlap in Late Antique Scientia},
  journal = {Nanzan University Anthropological Institute Working Papers},
  year    = {2026},
  month   = {July}
}
