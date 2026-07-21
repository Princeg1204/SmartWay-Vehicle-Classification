import joblib


# Model path
model_path = "models/smartway_random_forest_model.pkl"


# Load model
model = joblib.load(model_path)


print("Model Loaded Successfully ✅")

print(model)