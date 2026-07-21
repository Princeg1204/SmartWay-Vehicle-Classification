import joblib


scaler = joblib.load(
    "models/feature_scaler.pkl"
)


print("Scaler loaded successfully ✅")

print("\nScaler Type:")
print(type(scaler))


print("\nNumber of features scaler expects:")
print(scaler.n_features_in_)