"""
Random Forest–Based Feature Importance for
Machine-Learning–Assisted Groundwater Resilience Index (GRI)

This script demonstrates a generalized workflow for:
- Training a Random Forest model
- Estimating relative importance of groundwater parameters
- Evaluating model performance

The script is intentionally location-agnostic and uses
placeholder filenames. Users should replace input data
with their own datasets.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# ------------------------------------------------------
# USER INPUT (replace with your own dataset)
# ------------------------------------------------------

DATA_FILE = "sample_dataset.csv"   # placeholder CSV

FEATURES = ["DTWL", "WQI", "LULC", "LITHOLOGY"]
TARGET = "GRI"


# ------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------

data = pd.read_csv(DATA_FILE)

X = data[FEATURES]
y = data[TARGET]


# ------------------------------------------------------
# TRAIN–TEST SPLIT
# ------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)


# ------------------------------------------------------
# RANDOM FOREST MODEL
# ------------------------------------------------------

rf_model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)


# ------------------------------------------------------
# PREDICTION & PERFORMANCE
# ------------------------------------------------------

y_pred = rf_model.predict(X_test)

r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mae = mean_absolute_error(y_test, y_pred)

print("Model Performance")
print("-----------------")
print(f"R²   : {round(r2, 3)}")
print(f"RMSE : {round(rmse, 3)}")
print(f"MAE  : {round(mae, 3)}")


# ------------------------------------------------------
# FEATURE IMPORTANCE
# ------------------------------------------------------

importance = pd.DataFrame({
    "Parameter": FEATURES,
    "Importance": rf_model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance")
print("------------------")
print(importance)


# ------------------------------------------------------
# OPTIONAL PLOT
# ------------------------------------------------------

plt.figure(figsize=(6, 4))
plt.barh(importance["Parameter"], importance["Importance"])
plt.xlabel("Relative Importance")
plt.title("Random Forest Feature Importance (GRI)")
plt.tight_layout()
plt.show()
