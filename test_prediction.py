import joblib
import pandas as pd


model = joblib.load(
    "models/smartway_random_forest_model.pkl"
)


scaler = joblib.load(
    "models/feature_scaler.pkl"
)


# Load one sample from dataset
df = pd.read_csv(
    "data/smartway_ml_dataset.csv"
)


# Remove target column
X = df.drop("SmartWay", axis=1)


# Take first row
sample = X.iloc[[0]]


# Scale sample
sample_scaled = scaler.transform(sample)


# Prediction
prediction = model.predict(sample_scaled)


print("Prediction:")
print(prediction)