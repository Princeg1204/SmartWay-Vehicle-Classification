import pandas as pd


df = pd.read_csv(
    "data/smartway_ml_dataset.csv"
)


print("Categorical encoded columns:")

for col in df.columns:
    if "_" in col:
        print(col)