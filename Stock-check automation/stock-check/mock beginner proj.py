import pandas as pd

import pandas as pd

# --------------------------------------------------
# 1. Load dataset (You can replace this with your own CSV later)
# --------------------------------------------------
data = {
    "ItemID": ["A101", "A102", "A103", "A103", "A104", "A105", ""],
    "Label": ["Window Frame", "Glass Panel", "Parcel Box", "Parcel Box", "", "Sealant Pack", "UPVC Rod"],
    "Quantity": [50, 200, 120, 120, 75, 40, 60],
    "RecordedQty": [50, 198, 120, 120, 75, 39, 60],
}

df = pd.DataFrame(data)

print("\n=== RAW DATA ===")
print(df)

# --------------------------------------------------
# 2. Identify Errors
# --------------------------------------------------
errors = []

# Quantity mismatches
mismatch = df[df["Quantity"] != df["RecordedQty"]]
if not mismatch.empty:
    for _, row in mismatch.iterrows():
        errors.append({
            "ItemID": row["ItemID"],
            "Issue": "Quantity mismatch",
            "Details": f'{row["Quantity"]} vs {row["RecordedQty"]}'
        })

# Duplicate ItemIDs
duplicate_ids = df[df.duplicated("ItemID", keep=False)]
if not duplicate_ids.empty:
    for item in duplicate_ids["ItemID"].unique():
        errors.append({
            "ItemID": item,
            "Issue": "Duplicate ItemID",
            "Details": "Same ItemID appears multiple times"
        })

# Missing Labels
missing_labels = df[df["Label"] == ""]
if not missing_labels.empty:
    for _, row in missing_labels.iterrows():
        errors.append({
            "ItemID": row["ItemID"],
            "Issue": "Missing Label",
            "Details": "Label field is blank"
        })

# --------------------------------------------------
# 3. Convert errors into a DataFrame
# --------------------------------------------------
error_df = pd.DataFrame(errors)

print("\n=== DETECTED ERRORS ===")
print(error_df)

# --------------------------------------------------
# 4. Export to CSV for Power BI
# --------------------------------------------------
output_file = "stock_error_report.csv"
error_df.to_csv(output_file, index=False)

print(f"\n✔ Error report successfully saved as: {output_file}")
