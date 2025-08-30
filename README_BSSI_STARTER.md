# BSSI: Housing + Care Sync (NDIS/SRS & Aged Care)

Align new homes with **trustworthy support** using the **Build–Service Sync Index (BSSI)** and a **Social Impact Layer** for quality.

## Overview
- **BSSI (0–100)** = 0.5 · Coverage + 0.3 · Quality + 0.2 · Access  
- **Coverage**: providers per 1k residents (NDIS/SRS & aged-care), area‑level  
- **Access**: proximity to PT stops and key amenities  
- **Quality**: *prototype proxy* → **Social Impact Score (SIS)** via partial‑audit transparency

## Datasets (GovHack 2025 — Victoria)
- **Primary**: Victoria Building Permit Activity Monthly Summaries (VBA) — used to compute a 12‑month permits index for Outer Melbourne (evidence CSVs included).
- **Optional layers**: PTV stops, School Locations, ABS SEIFA (not required to reproduce the demo CSV).

## Files in this repo (starter)
- `VBA_12mo_region_summary.csv` — 12‑month permit totals and a scaled index (0–100) for Inner/Outer/Rural Melbourne  
- `VBA_monthly_region_timeseries.csv` — monthly permit counts by Region (evidence)  
- `PatDream_BSSI_demo_points_TEMPLATE.csv` — 5 demo suburbs with placeholder access/coverage/quality (no permits index)  
- `bssi_compute.py` — recomputes BSSI and injects the permits index into a demo CSV

## Reproduce (local)
1. Ensure the four CSV/script files are in the same folder.
2. Run:
   ```bash
   python bssi_compute.py
   ```
3. Output: `output/PatDream_BSSI_demo_points_COMPUTED.csv` with:
   - `Permits_Growth_Index_0_100` set from the **Outer Melbourne** row in `VBA_12mo_region_summary.csv`
   - `BSSI_0_100 = 0.5*Coverage_per_1k + 0.3*QualityProxy_0_100 + 0.2*Access_0_100`

## How to map (Google My Maps)
- Import `output/PatDream_BSSI_demo_points_COMPUTED.csv`
- Geocode by: **Suburb, State, Country**; Label by **Suburb**
- Style by **BSSI_0_100** (or `Permits_Growth_Index_0_100`), share as *Anyone with the link can view*

## Ethics, Privacy & Fairness
- Area‑level publishing only; suppress small‑N cells; de‑identify all counts/ratios
- Open methodology and versioned releases; providers have a right‑of‑reply on audit summaries
- SIS replaces proxies with **partial‑audit transparency**; formulas are explainable

## License
MIT (or your preferred open license).
