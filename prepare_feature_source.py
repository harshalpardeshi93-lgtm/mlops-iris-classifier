import pandas as pd
from pathlib import Path

# Practical 4 input file
input_file = Path(
    "data/processed/iris_features.csv"
)

# Feast output file
output_file = Path(
    "practical5_feast/iris_feature_repo/feature_repo/data/iris_features.parquet"
)

# Read feature-engineered data
df = pd.read_csv(input_file)

# Create entity ID
df.insert(0, "sample_id", range(len(df)))

# Create event timestamps
start_time = pd.Timestamp(
    "2026-08-15 15:20:02",
    tz="UTC"
)

df["event_timestamp"] = pd.date_range(
    start=start_time,
    periods=len(df),
    freq="min"
)

# Created timestamp
df["created_timestamp"] = df["event_timestamp"]

# Create output directory
output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)

# Save as Parquet
df.to_parquet(
    output_file,
    index=False
)

print(f"Wrote {len(df)} rows to {output_file}")