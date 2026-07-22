import sklearn
print("=" * 50)
print("Scikit-learn Version:", sklearn.__version__)
print("=" * 50)

import pandas as pd
import joblib

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier

print("=" * 80)
print("CREATING NEW SMARTWAY PIPELINE")
print("=" * 80)

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

df = pd.read_csv("data/smartway_cleaned_dataset.csv")

print("Dataset Loaded Successfully")
print(df.shape)

# ---------------------------------------------------
# Features & Target
# ---------------------------------------------------

X = df.drop(
    columns=[
        "SmartWay",
        "Model",
        "Underhood ID"
    ]
)

y = df["SmartWay"]

# ---------------------------------------------------
# Categorical Columns
# ---------------------------------------------------

categorical_cols = [
    "Drive",
    "Fuel",
    "Stnd",
    "Trans",
    "Veh Class"
]

# ---------------------------------------------------
# Numerical Columns
# ---------------------------------------------------

numerical_cols = [
    col for col in X.columns
    if col not in categorical_cols
]

# ---------------------------------------------------
# Preprocessor
# ---------------------------------------------------

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            StandardScaler(),
            numerical_cols
        ),
        (
            "cat",
            OneHotEncoder(
                drop="first",
                handle_unknown="ignore"
            ),
            categorical_cols
        )
    ]
)

# ---------------------------------------------------
# Pipeline
# ---------------------------------------------------

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    ))
])

# ---------------------------------------------------
# Train
# ---------------------------------------------------

print("Training Pipeline...")

pipeline.fit(X, y)

print("Training Completed")

# ---------------------------------------------------
# Save
# ---------------------------------------------------

joblib.dump(
    pipeline,
    "models/smartway_pipeline.pkl"
)

print("\nPipeline Saved Successfully")
print("models/smartway_pipeline.pkl")