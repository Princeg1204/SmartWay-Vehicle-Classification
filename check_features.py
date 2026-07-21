import joblib


model = joblib.load(
    "models/smartway_random_forest_model.pkl"
)


print("Number of features:")
print(model.n_features_in_)


print("\nFeature names:")
print(model.feature_names_in_)