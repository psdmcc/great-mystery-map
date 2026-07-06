#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import json
import os
import base64

input_file = "mysterium_geospatial_vectors.csv"
output_html = "mysterium_interactive_map.html"

def main():
    print("="*60)
    print("MYSTERIUM GEOSPATIAL VECTOR COMPILER ONLINE")
    print("="*60)
    
    if not os.path.exists(input_file):
        print(f"[!] Error: Cannot find '{input_file}'. Run analytics script first.")
        return

    rows_data = []
    with open(input_file, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lat = float(row.get("Latitude_Vector", 0.0))
                lon = float(row.get("Longitude_Vector", 0.0))
                if lat != 0.0 and lon != 0.0:
                    work = row.get("Work_Title", "Unknown Work").strip().replace("\n", " ")
                    site = row.get("ToposText_Ancient_Site", "Unknown Site").strip().replace("\n", " ")
                    themes = row.get("Overlapping_Themes", "N/A").strip().replace("\n", " ")
                    keywords = row.get("Greek_Keywords", "N/A").strip().replace("\n", " ")
                    snippet = row.get("Greek_Context_Snippet", "N/A").strip().replace("\n", " ")
                    url = row.get("Perseus_Web_URL", "#").strip()
                    
                    rows_data.append({
                        "work": " ".join(work.split()),
                        "site": " ".join(site.split()),
                        "lat": lat,
                        "lon": lon,
                        "themes": " ".join(themes.split()),
                        "keywords": " ".join(keywords.split()),
                        "snippet": " ".join(snippet.split()),
                        "url": url
                    })
            except ValueError:
                continue

    # Convert the payload into a completely safe Base64 string asset
    json_bytes = json.dumps(rows_data, ensure_ascii=False).encode('utf-8')
    b64_payload = base64.b64encode(json_bytes).decode('utf-8')

    html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Mysterium Magnum Interactive Geospatial Map</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Verified production library assets with high-integrity matching flags -->
    <link rel="stylesheet" href="https://cloudflare.com" crossorigin="" />
    <script src="https://cloudflare.com" crossorigin=""></script>
    
    <link rel="stylesheet" href="https://cloudflare.com" crossorigin="" />
    <link rel="stylesheet" href="https://cloudflare.com" crossorigin="" />
    <script src="https://cloudflare.com" crossorigin=""></script>
    
    <style>
        html, body, #map { width: 100%; height: 100%; margin: 0; padding: 0; background: #fafafa; }
        .popup-box { font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 12px; width: 300px; line-height: 1.4; color: #2c3e50; }
        .popup-title { color: #d32f2f; margin: 0 0 6px 0; font-size: 13px; border-bottom: 2px solid #ef5350; padding-bottom: 4px; font-weight: bold; }
        .theme-tag { background: #e3f2fd; color: #0d47a1; padding: 2px 5px; border-radius: 3px; font-size: 10px; font-weight: bold; display: inline-block; }
        .snippet-box { margin: 8px 0; padding: 8px; background: #f5f5f5; border-left: 4px solid #b0bec5; font-style: italic; max-height: 90px; overflow-y: auto; white-space: normal; word-break: break-word; line-height: 1.5; color: #34495e; text-align: left; }
        .btn-link { background: #1976d2; color: white !important; padding: 5px 10px; border-radius: 3px; text-decoration: none; font-size: 11px; font-weight: bold; float: right; margin-top: 4px; }
    </style>
</head>
<body>
    <div id="map"></div>
    <script>
        // Initialize map engine layout
        var map = L.map('map').setView([38.5, 24.5], 5);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap contributors'
        }).add_to(map);

        var markers = L.markerClusterGroup({ maxClusterRadius: 40 });
        
        // Base64 decoding string container
        var b64Data = \"""" + b64_payload + """\";
        
        try {
            var decodedJson = decodeURIComponent(atob(b64Data).split('').map(function(c) {
                return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
            }).join(''));
            
            var mapData = JSON.parse(decodedJson);

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
        } catch(e) {
            console.error("Mapping failure: ", e);
        }
    </script>
</body>
</html>
"""
    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[✔] Success! Highly resilient map file compiled to '{output_html}'.")

if __name__ == '__main__':
    main()
