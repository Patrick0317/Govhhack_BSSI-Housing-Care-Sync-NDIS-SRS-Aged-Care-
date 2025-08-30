# Minimal BSSI demo computation
# Usage: python bssi_compute.py
import os
import pandas as pd

# Inputs
permits_csv = "VBA_12mo_region_summary.csv"
demo_csv_in = "PatDream_BSSI_demo_points_TEMPLATE.csv"
os.makedirs("output", exist_ok=True)
demo_csv_out = os.path.join("output", "PatDream_BSSI_demo_points_COMPUTED.csv")

# 1) Read permits summary and pick Outer Melbourne index (0–100)
permits = pd.read_csv(permits_csv)
outer_idx = int(permits.loc[permits["Region"]=="Outer Melbourne","Permits_Growth_Index_0_100"].iloc[0])

# 2) Read demo points (template has no permits index or BSSI yet)
df = pd.read_csv(demo_csv_in)

# 3) Inject permits index + compute BSSI
df["Permits_Growth_Index_0_100"] = outer_idx
df["BSSI_0_100"] = (
    0.5*df["Coverage_per_1k"] +
    0.3*df["QualityProxy_0_100"] +
    0.2*df["Access_0_100"]
).round(0).astype(int)

# 4) Save
df.to_csv(demo_csv_out, index=False)
print("Wrote:", demo_csv_out)
