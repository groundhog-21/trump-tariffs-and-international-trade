# Data documentation

## Included source snapshot

- **File:** [`raw/FTD-mf.csv`](raw/FTD-mf.csv), included to reproduce this analysis without a separate download.
- **Publisher:** US Census Bureau, [International Trade](https://www.census.gov/foreign-trade/index.html).
- **Format:** Multi-section CSV with category, measure, geography, and period lookup tables followed by a `DATA` section.
- **File size:** 55,075 bytes.
- **Source-stated update:** September 3, 2026. This is not a verified download date.
- **Provenance limitation:** The exact original export URL and download date were not recorded. This saved snapshot is the input used for the published analysis; a later Census export may contain revisions or additional months.

## Series used

The notebook selects US goods on a balance-of-payments basis (`cat_idx = 2`, `geo_idx = 1`, `is_adj = 0`), with imports, exports, and trade balance measured in millions of US dollars. The combined goods-and-services category is excluded. Values are not inflation-adjusted.

The selected series contain 415 complete monthly observations from January 1992 through July 2026. Although the period lookup lists later months, they have no observations in this snapshot.

## Preparation and reproduction

1. Run `notebooks/data_understanding_and_preparation.ipynb` from top to bottom. It reads the included source file, joins readable dates, and reshapes the selected series into one row per month.
2. The notebook checks completeness through non-null counts and retains complete imports, exports, and trade balance records.
3. It computes 12-month percentage changes for imports and exports, and a 12-month dollar change for trade balance. The first 12 months have no prior-year observations, so their YoY values are undefined. They are dropped rather than imputed, leaving 403 complete observations from January 1993 through July 2026.
4. The second-term indicator is 1 from January 2025 onward and 0 before then. January 2025 is included in full: 19 second-term observations and 384 earlier observations remain.
5. The notebook writes `processed/analysis_data.csv`, including the date index. Run `notebooks/modeling_and_evaluation.ipynb` next to load that generated file.

The processed file is excluded from Git because it is reproducible from the included raw snapshot. Preserve the snapshot when reproducing the published results; use a separately named file for any future update.

## Attribution

Source data: US Census Bureau. This project is an independent analysis and does not imply Census Bureau endorsement.

## Snapshot integrity

SHA-256 of `raw/FTD-mf.csv`:

b2bc09cd992abfaa71edf63af574a591dd22efc56989d81fe82982f43c599b31

