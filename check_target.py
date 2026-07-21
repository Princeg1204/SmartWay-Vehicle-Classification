import pandas as pd


df = pd.read_csv(
    "data/smartway_ml_dataset.csv"
)


print("SmartWay value counts:")
print(df["SmartWay"].value_counts())


print("\nData type:")
print(df["SmartWay"].dtype)