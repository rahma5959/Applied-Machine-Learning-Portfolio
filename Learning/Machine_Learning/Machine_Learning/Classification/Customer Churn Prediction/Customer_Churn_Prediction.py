import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

# Data generation

np.random.seed(42)
n_samples = 1000
data = pd.DataFrame({
    "contract_length": np.random.randint(1, 36, n_samples),        # months with company
    "monthly_cost": np.random.uniform(20, 100, n_samples),          # subscription cost
    "support_calls": np.random.randint(0, 10, n_samples),           # number of support calls
    "data_usage": np.random.uniform(1, 50, n_samples),              # GB per month
    "late_payments": np.random.randint(0, 5, n_samples),            # number of late payments
    "has_premium": np.random.choice([0, 1], n_samples)              # premium subscription
})


logit = (
     
    0.05 * data["contract_length"] - 
    0.03 * data["monthly_cost"] + 
    0.2 * data["support_calls"] + 
    0.01 * data["data_usage"] + 
    0.3 * data["late_payments"] + 
    0.5 * data["has_premium"]+
    np.random.normal(0, 1, n_samples)
)

prob=1/(1+np.exp(-logit))
data["churn"] = np.random.binomial(1, prob)

# Features / Target
X = data.drop("churn", axis=1)
y = data["churn"]

# Train / Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=[0,1])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Logistic Regression")
plt.savefig("result.png", dpi=300)
plt.show()