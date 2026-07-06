import csv
import os

# Natively writing build_map_standalone.py into your workspace folder
code_content = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import os

INPUT_FILE = "mysterium_geospatial_vectors.csv"
OUTPUT_HTML = "mysterium_interactive_map.html"

def main():
    print("="*60)
    print("MYSTERIUM HIGH-FIDELITY STANDALONE MAP COMPILER ONLINE")
    print("="*60)
    
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: Cannot locate data grid '{INPUT_FILE}'.")
        return

    rows_data = []
    with open(INPUT_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lat = float(row.get("Latitude_Vector", 0.0))
                lon = float(row.get("Longitude_Vector", 0.0))
                if lat != 0.0 and lon != 0.0:
                    work = row.get("Work_Title", "Unknown Work").replace("'", "\\\\'").replace('"', '\\\\"').replace('\\n', ' ').strip()
                    work = " ".join(work.split())
                    site = row.get("ToposText_Ancient_Site", "Unknown Site").replace("'", "\\\\'").replace('"', '\\\\"').strip()
                    themes = row.get("Overlapping_Themes", "N/A").replace("'", "\\\\'").replace('"', '\\\\"').strip()
                    keywords = row.get("Greek_Keywords", "N/A").replace("'", "\\\\'").replace('"', '\\\\"').strip()
                    snippet = row.get("Greek_Context_Snippet", "N/A").replace("'", "\\\\'").replace('"', '\\\\"').strip()
                    url = row.get("Perseus_Web_URL", "#").strip()
                    
                    rows_data.append({
                        "work": work, "site": site, "lat": lat, "lon": lon,
                        "themes": themes, "keywords": keywords, "snippet": snippet, "url": url
                    })
            except ValueError:
                continue

    if not rows_data:
        print("[!] No valid geospatial vector row blocks parsed from source ledger.")
        return

    html_content = \"\"\"<!DOCTYPE html>
<html>
<head>
    <title>Mysterium Magnum Interactive Geospatial Map</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com" />
    <script src="https://unpkg.com"></script>
    <link rel="stylesheet" href="https://unpkg.com" />
    <link rel="stylesheet" href="https://unpkg.com" />
    <script src="https://unpkg.com"></script>
    <style>
        html, body, #map { width: 100%; height: 100%; margin: 0; padding: 0; background: #fafafa; }
        .popup-box { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; width: 300px; line-height: 1.4; color: #2c3e50; }
        .popup-title { color: #d32f2f; margin: 0 0 6px 0; font-size: 13px; border-bottom: 2px solid #ef5350; padding-bottom: 4px; font-weight: bold; }
        .theme-tag { background: #e3f2fd; color: #0d47a1; padding: 2px 5px; border-radius: 3px; font-size: 10px; font-weight: bold; display: inline-block; }
        .snippet-box { margin: 8px 0; padding: 8px; background: #f5f5f5; border-left: 4px solid #b0bec5; font-style: italic; max-height: 90px; overflow-y: auto; white-space: normal; word-break: break-word; line-height: 1.5; color: #34495e; text-align: left; }
        .btn-link { background: #1976d2; color: white !important; padding: 5px 10px; border-radius: 3px; text-decoration: none; font-size: 11px; font-weight: bold; float: right; margin-top: 4px; transition: background 0.2s; }
        .btn-link:hover { background: #1565c0; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        var map = L.map('map').setView([38.5, 24.5], 5);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap contributors'
        }).add_to(map);

        var markers = L.markerClusterGroup({ maxClusterRadius: 40 });
        var mapData = [
\"\"\"

    for r in rows_data:
        html_content += f\"\"\"            {{
                work: "{r['work']}", site: "{r['site']}", lat: {r['lat']}, lon: {r['lon']},
                themes: "{r['themes']}", keywords: "{r['keywords']}", snippet: "{r['snippet']}", url: "{r['url']}"
            }},
\"\"\"

    html_content += \"\"\"        ];

        mapData.forEach(function(r) {
            var html = '<div class="popup-box">' +
                       '<div class="popup-title">' + r.work + '</div>' +
                       '<div><b>Ancient Site:</b> ' + r.site + ' (' + r.lat.toFixed(3) + ', ' + r.lon.toFixed(3) + ')</div>' +
                       '<div style="margin:5px 0;"><b>Themes:</b> <span class="theme-tag">' + r.themes + '</span></div>' +
                       '<div><b>Keywords:</b> <span style="color:#2e7d32; font-weight:bold;">' + r.keywords + '</span></div>' +
                       '<div class="snippet-box">' + r.snippet + '</div>' +
                       '<a href="' + r.url + '" target="_blank" class="btn-link">Launch Scaife Viewer &rarr;</a>' +
                       '</div>';
            var marker = L.marker([r.lat, r.lon]).bindPopup(html);
            markers.addLayer(marker);
        });

        map.addLayer(markers);
    </script>
</body>
</html>\"\"\"

    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    print(f"[✔] Success! Leaflet Geospatial Web Map compiled cleanly to '{OUTPUT_HTML}'.")
    print("="*60)

if __name__ == "__main__":
    main()
"""

with open("build_map_standalone.py", "w", encoding="utf-8") as f:
    f.write(code_content)
