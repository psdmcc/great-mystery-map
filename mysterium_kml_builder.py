#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import os
import xml.sax.saxutils as saxutils

INPUT_FILE = "mysterium_geospatial_vectors.csv"
OUTPUT_FILE = "mysterium_globe.kml"

def main():
    if not os.path.exists(INPUT_FILE):
        return

    count = 0
    placemarks_buffer = []

    with open(INPUT_FILE, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                lat_str = row.get("Latitude_Vector", "0").strip()
                lon_str = row.get("Longitude_Vector", "0").strip()
                lat = float(lat_str) if lat_str else 0.0
                lon = float(lon_str) if lon_str else 0.0
                
                if lat != 0.0 and lon != 0.0:
                    if lat < 30.0 and lon > 30.0:
                        lat, lon = lon, lat
                        
                    work_text = saxutils.escape(row.get("Work_Title", "Unknown Work").strip())
                    site_text = row.get("ToposText_Ancient_Site", "Unknown Site").strip()
                    themes_text = row.get("Overlapping_Themes", "N/A").strip()
                    snippet_text = row.get("Greek_Context_Snippet", "N/A").strip()
                    
                    desc_html_body = f"<b>Ancient Site:</b> {site_text}<br/><b>Themes:</b> {themes_text}<br/><br/><i>{snippet_text}</i>"
                    
                    placemark_block = f"""  <Placemark>
    <name>{work_text}</name>
    <description><![CDATA[{desc_html_body}]]></description>
    <Point>
      <coordinates>{lon},{lat},0</coordinates>
    </Point>
  </Placemark>"""
                    
                    placemarks_buffer.append(placemark_block)
                    count += 1
            except Exception as e:
                continue

    # Stripping the <kml> wrapper entirely
    kml_output_content = (
        '<Document>\n'
        '  <name>Mysterium Magnum Coordinates</name>\n'
        + "\n".join(placemarks_buffer) + "\n"
        '</Document>\n'
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(kml_output_content)

if __name__ == '__main__':
    main()
