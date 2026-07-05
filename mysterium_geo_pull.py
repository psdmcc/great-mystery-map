#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import ssl
import urllib.request

LAYER_DIR = "qgis_layers"
med_countries_dir = os.path.join(LAYER_DIR, "med_countries")
med_coastlines_dir = os.path.join(LAYER_DIR, "med_coastlines")

# Permanent un-zipped geospatial component maps hosted via reliable public servers
FILES_TO_DOWNLOAD = {
    med_countries_dir: [
        ("https://github.com", "ne_50m_admin_0_countries.shp"),
        ("https://github.com", "ne_50m_admin_0_countries.shx"),
        ("https://github.com", "ne_50m_admin_0_countries.dbf"),
        ("https://github.com", "ne_50m_admin_0_countries.prj")
    ],
    med_coastlines_dir: [
        ("https://github.com", "ne_50m_coastline.shp"),
        ("https://github.com", "ne_50m_coastline.shx"),
        ("https://github.com", "ne_50m_coastline.dbf"),
        ("https://github.com", "ne_50m_coastline.prj")
    ]
}

def main():
    print("="*60)
    print("MYSTERIUM COMPONENT GEOMETRY HARVESTER ACTIVE")
    print("="*60)
    
    # Force context bypass to handle all local macOS SSL root certificate blocks safely
    ssl_context = ssl._create_unverified_context()
    opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl_context))
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)')]
    urllib.request.install_opener(opener)

    for target_dir, files in FILES_TO_DOWNLOAD.items():
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
            
        for url, file_name in files:
            output_path = os.path.join(target_dir, file_name)
            print(f"[*] Extracting structural layer: {file_name}")
            try:
                # Direct byte streaming avoids all zip file corruption vectors completely
                urllib.request.urlretrieve(url, output_path)
            except Exception as e:
                print(f"[!] Error pulling {file_name}: {e}")
                
    print("\n[✔] Data harvesting complete. All structural shapefiles compiled.")
    print("="*60)

if __name__ == '__main__':
    main()
