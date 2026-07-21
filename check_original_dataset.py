import pandas as pd


df = pd.read_csv(
    "data/smartway_cleaned_dataset.csv"
)


print("Dataset Shape:")
print(df.shape)


print("\nColumns:")
for i, col in enumerate(df.columns):
    print(i, ":", col)