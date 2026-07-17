import pandas as pd
import os

def rank_high_density_sources(csv_path="echidna_salvation_matrix.csv"):
    if not os.path.exists(csv_path):
        print(f"[-] Data file '{csv_path}' not found.")
        return

    print("[*] Grouping and ranking your 1,921 text intersections by document source...")
    df = pd.read_csv(csv_path)
    
    # Calculate frequency counts per document
    ranking = df['Source_Document'].value_counts().reset_index()
    ranking.columns = ['Document_Name', 'Intersection_Count']
    
    # Calculate percentage contributions
    total_hits = len(df)
    ranking['Percentage_of_Total'] = (ranking['Intersection_Count'] / total_hits * 100).round(2)
    
    print("\n📊 Top 10 High-Density Text Environments for the Echidna-Salvation Matrix")
    print("=" * 75)
    print(f"{'Rank':<4} | {'Document / Author Asset File':<42} | {'Hits':<5} | {'Share %'}")
    print("-" * 75)
    
    for idx, row in ranking.head(10).iterrows():
        print(f" {idx+1:<3} | {row['Document_Name']:<42} | {row['Intersection_Count']:<5} | {row['Percentage_of_Total']}%")
    print("=" * 75)
    
    # Save the full ranking ledger for your Section 7 data references
    ranking.to_csv("echidna_source_rankings.csv", index=False)
    print("[+] Full distribution map successfully compiled inside 'echidna_source_rankings.csv'.")

if __name__ == "__main__":
    rank_high_density_sources()
