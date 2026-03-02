import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_csv(path):
    """Load CSV file as DataFrame."""
    return pd.read_csv(path)

def scale_features(X_train, X_test):
    """Scale features using StandardScaler."""
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler