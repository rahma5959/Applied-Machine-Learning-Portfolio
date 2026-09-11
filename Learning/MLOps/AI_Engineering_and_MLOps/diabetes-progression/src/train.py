# train.py
import time

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
import mlflow
import mlflow.sklearn

from config import load_config

config = load_config()

# Charger le dataset
diabetes = load_diabetes()
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.Series(diabetes.target, name="target")

# Split train/validation/test
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

# Standardisation
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Définir les modèles
models = {
    "LinearRegression": LinearRegression(),
    "Ridge": Ridge(alpha=1.0),
    "Lasso": Lasso(alpha=0.1),
    "RandomForest": RandomForestRegressor(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingRegressor(n_estimators=100, random_state=42),
    "XGBoost": XGBRegressor(n_estimators=100, random_state=42, eval_metric='rmse')
}

results = {}
kf = KFold(n_splits=5, shuffle=True, random_state=42)
mlflow.set_experiment("diabetes_regression")

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        mlflow.log_params(model.get_params())
        start_time = time.time() 

        cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=kf, scoring='r2')

        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_val_scaled)

        mae = mean_absolute_error(y_val, y_pred)
        rmse = np.sqrt(mean_squared_error(y_val, y_pred))
        r2 = r2_score(y_val, y_pred)

        mlflow.log_metric("CV_R2_mean", np.mean(cv_scores))
        mlflow.log_metric("MAE", mae)
        mlflow.log_metric("RMSE", rmse)
        mlflow.log_metric("R2", r2)

        execution_time = time.time() - start_time  
        mlflow.log_metric("execution_time_sec", execution_time)  

        results[name] = {"CV_R2_mean": np.mean(cv_scores), "MAE": mae, "RMSE": rmse, "R2": r2}

        print(f"\n{name} results:")
        print(f"  CV R2 mean: {np.mean(cv_scores):.4f}")
        print(f"  MAE: {mae:.4f}, RMSE: {rmse:.4f}, R2: {r2:.4f}")

        mlflow.sklearn.log_model(model, "model")

        if name in ["RandomForest", "GradientBoosting", "XGBoost"]:
            importances = model.feature_importances_
            feature_importance_df = pd.DataFrame({
                "feature": X.columns,
                "importance": importances
            }).sort_values(by="importance", ascending=False)
            print("\nFeature importances:")
            print(feature_importance_df)

            # Feature importance plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.barh(feature_importance_df["feature"], feature_importance_df["importance"])
            ax.invert_yaxis()
            ax.set_title(f"{name} Feature Importance")
            mlflow.log_figure(fig, "feature_importance.png")
            plt.close(fig)

            # SHAP plot
            explainer = shap.Explainer(model, X_train_scaled)
            shap_values = explainer(X_test_scaled, check_additivity=False)
            shap.summary_plot(shap_values, X_test, plot_type="bar", show=False)
            mlflow.log_figure(plt.gcf(), "shap_summary.png")
            plt.close()

# Sauvegarder le scaler
joblib.dump(scaler, config["paths"]["scaler_path"])
print("\nScaler saved!")

# ------------------------------
# Petit test rapide MLflow
# ------------------------------
with mlflow.start_run(run_name="test_plot"):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])
    ax.set_title("Test Plot")
    mlflow.log_figure(fig, "test_plot.png")
    plt.close(fig)
print("\nPetit test terminé. Vérifie le run 'test_plot' dans MLflow UI.")