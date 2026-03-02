# train.py
import pandas as pd
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import shap
import matplotlib.pyplot as plt
import joblib

from config import load_config

config=load_config()
# Load the built-in diabetes dataset
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.Series(diabetes.target, name="target")

# Split into train, validation and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Define models
models = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.1),
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=42, eval_metric='rmse')
}

# Train and evaluate models
results = {}
kf = KFold(n_splits=5, shuffle=True, random_state=42)

for name, model in models.items():
    cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=kf, scoring='r2')
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_val_scaled)
    mae = mean_absolute_error(y_val, y_pred)
    rmse = mean_squared_error(y_val, y_pred)
    r2 = r2_score(y_val, y_pred)
    
    results[name] = {
        "CV_R2_mean": np.mean(cv_scores),
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }
    
    print(f"\n{name} results:")
    print(f"  CV R2 mean: {np.mean(cv_scores):.4f}")
    print(f"  MAE: {mae:.4f}, RMSE: {rmse:.4f}, R2: {r2:.4f}")

# Find the best model
best_model_name = max(results, key=lambda k: results[k]["R2"])
best_model = models[best_model_name]
print(f"\nBest model based on validation R2: {best_model_name}")

# Feature importance for tree models
if best_model_name in ["RandomForest", "GradientBoosting", "XGBoost"]:
    importances = best_model.feature_importances_
    feature_importance_df = pd.DataFrame({"feature": X.columns, "importance": importances}).sort_values(by="importance", ascending=False)
    print("\nFeature importances:")
    print(feature_importance_df)
    
    plt.figure(figsize=(10,6))
    plt.barh(feature_importance_df["feature"], feature_importance_df["importance"])
    plt.gca().invert_yaxis()
    plt.title(f"{best_model_name} Feature Importance")
    plt.show()
    
    explainer = shap.Explainer(best_model, X_train_scaled)
    shap_values = explainer(X_test_scaled)
    shap.summary_plot(shap_values, X_test, plot_type="bar")

# Save the model and scaler
joblib.dump(best_model, config["paths"]["model_path"])
joblib.dump(scaler, config["paths"]["scaler_path"])
print("\nModel and scaler saved!")