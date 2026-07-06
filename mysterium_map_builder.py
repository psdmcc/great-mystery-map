#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mysterium_map_builder.py
Production-Grade Interactive Geospatial Map Builder.
Ingests ToposText coordinates, clusters regional data, and compiles a responsive
HTML map file embedded with Greek context snippets and Scaife deep-links.
"""

import csv
import os
import re

INPUT_FILE = "mysterium_geospatial_vectors.csv"
OUTPUT_HTML = "mysterium_interactive_map.html"

def main():
    print("="*60)
    print("MYSTERIUM HIGH-FIDELITY GEOSPATIAL MAP BUILDER ONLINE")
    print("="*60)
    
    if not os.path.exists(INPUT_FILE):
        print(f"[!] Error: Cannot locate source data file '{INPUT_FILE}'.")
        return

    # Check for folium library, fallback to native high-density HTML compiler if missing
    try:
        import folium
        from folium.plugins import MarkerCluster
        print("[+] Folium library detected. Initiating high-resolution Leaflet map layer...")
        use_folium = True
    except ImportError:
        print("[*] Folium library not found locally. Automatically running native script compiler pass...")
        use_folium = False

    rows_data = []
    with open(INPUT_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lat = float(row.get("Latitude_Vector", 0.0))
                lon = float(row.get("Longitude_Vector", 0.0))
                if lat != 0.0 and lon != 0.0:
                    rows_data.append({
                        "work": row.get("Work_Title", "Unknown Work").replace("'", "\\'"),
                        "site": row.get("ToposText_Ancient_Site", "Unknown Site").replace("'", "\\'"),
                        "lat": lat,
                        "lon": lon,
                        "themes": row.get("Overlapping_Themes", "N/A").replace("'", "\\'"),
                        "keywords": row.get("Greek_Keywords", "N/A").replace("'", "\\'"),
                        "snippet": row.get("Greek_Context_Snippet", "N/A").replace("'", "\\'"),
                        "url": row.get("Perseus_Web_URL", "#")
                    })
            except ValueError:
                continue

    if not rows_data:
        print("[!] No valid geospatial vector rows found. Re-run your mapping engine files.")
        return

    if use_folium:
        # Build map with beautiful open-source terrain styles
        m = folium.Map(location=[38.0, 24.0], zoom_start=5, tiles="OpenStreetMap")
        marker_cluster = MarkerCluster().add_to(m)

        for r in rows_data:
            popup_html = f"""
            <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 12px; width: 320px; line-height: 1.4;">
                <h4 style="margin: 0 0 5px 0; color: #d32f2f; font-size: 14px; border-bottom: 2px solid #ef5350; padding-bottom: 3px;">{r['work']}</h4>
                <p style="margin: 5px 0;"><b>ToposText Site:</b> {r['site']} ({r['lat']:.4f}, {r['lon']:.4f})</p>
                <p style="margin: 5px 0;"><b>Categories:</b> <span style="background-color: #e3f2fd; color: #0d47a1; padding: 2px 4px; border-radius: 3px; font-size: 10px; font-weight: bold;">{r['themes']}</span></p>
                <p style="margin: 5px 0;"><b>Keywords:</b> <span style="color: #2e7d32; font-weight: bold;">{r['keywords']}</span></p>
                <div style="margin: 8px 0; padding: 8px; background-color: #f5f5f5; border-left: 4px solid #b0bec5; font-style: italic; font-size: 11.5px; direction: ltr; text-align: left; max-height: 80px; overflow-y: auto;">
                    {r['snippet']}
                </div>
                <p style="margin: 5px 0 0 0; text-align: right;"><a href="{r['url']}" target="_blank" style="background-color: #1976d2; color: white; padding: 4px 8px; border-radius: 3px; text-decoration: none; font-size: 11px; font-weight: bold;">Launch Scaife Viewer ↗</a></p>
            </div>
            """
            folium.Marker(
                location=[r['lat'], r['lon']],
                popup=folium.Popup(popup_html, max_width=350),
                tooltip=f"{r['work']} ({r['site']})",
                icon=folium.Icon(color="red" if "galen" in r['work'].lower() else "blue", icon="info-sign")
            ).add_to(marker_cluster)

        m.save(OUTPUT_HTML)
    else:
        # Standalone Resilient HTML Engine pass to build the map without external python dependencies
        html_content = """<!DOCTYPE html>
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
        html, body, #map { width: 100%; height: 100%; margin: 0; padding: 0; }
        .popup-box { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; width: 300px; line-height: 1.4; }
        .popup-title { color: #d32f2f; margin: 0 0 6px 0; font-size: 13.5px; border-bottom: 2px solid #ef5350; padding-bottom: 3px; font-weight: bold; }
        .theme-tag { background: #e3f2fd; color: #0d47a1; padding: 2px 5px; border-radius: 3px; font-size: 10px; font-weight: bold; }
        .snippet-box { margin: 8px 0; padding: 8px; background: #f5f5f5; border-left: 4px solid #b0bec5; font-style: italic; max-height: 80px; overflow-y: auto; white-space: normal; word-break: break-word; }
        .btn-link { background: #1976d2; color: white; padding: 4px 8px; border-radius: 3px; text-decoration: none; font-size: 11px; font-weight: bold; float: right; margin-top: 4px; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        var map = L.map('map').setView([38.0, 24.0], 5);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '© OpenStreetMap contributors'
        }).add_to(map);

        var markers = L.markerClusterGroup();
        var data = [
        """
        for r in rows_data:
            html_content += f"""
            {{
                work: '{r["work"]}', site: '{r["site"]}', lat: {r["lat"]}, lon: {r["lon"]},
                themes: '{r["themes"]}', keywords: '{r["keywords"]}', snippet: '{r["snippet"]}', url: '{r["url"]}'
            }},"""
            
        html_content += """
        ];

        data.forEach(function(r) {
            var html = '<div class="popup-box">' +
                       '<div class="popup-title">' + r.work + '</div>' +
                       '<div><b>Site:</b> ' + r.site + ' (' + r.lat.toFixed(3) + ', ' + r.lon.toFixed(3) + ')</div>' +
                       '<div style="margin:4px 0;"><b>Themes:</b> <span class="theme-tag">' + r.themes + '</span></div>' +
                       '<div><b>Keywords:</b> <span style="color:#2e7d32; font-weight:bold;">' + r.keywords + '</span></div>' +
                       '<div class="snippet-box">' + r.snippet + '</div>' +
                       '<a href="' + r.url + '" target="_blank" class="btn-link">Launch Scaife Viewer ↗</a>' +
                       '</div>';
            var marker = L.marker([r.lat, r.lon]).bindPopup(html);
            markers.addLayer(marker);
        });

        map.addLayer(markers);
    </script>
</body>
</html>
"""
        with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
            f.write(html_content)

    print(f"[+] Success! Interactive geographic map cleanly generated and saved to '{OUTPUT_HTML}'.")
    print("="*60)

if __name__ == "__main__":
    main()
