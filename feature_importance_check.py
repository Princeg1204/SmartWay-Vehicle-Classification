import joblib
import pandas as pd


model = joblib.load(
    "models/smartway_random_forest_model.pkl"
)


importance = pd.DataFrame({
    "Feature_Index": range(len(model.feature_importances_)),
    "Importance": model.feature_importances_
})


importance = importance.sort_values(
    by="Importance",
    ascending=False
)


print(importance.head(20))