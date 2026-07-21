import pandas as pd


df = pd.read_csv(
    "data/smartway_cleaned_dataset.csv"
)


for col in df.columns:
    print("\n====================")
    print(col)
    print("Unique values:", df[col].nunique())

    if df[col].dtype == "object":
        print(df[col].unique()[:10])