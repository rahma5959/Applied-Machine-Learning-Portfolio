
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay


#  Data generation 

np.random.seed(42)
n_samples = 400

data = pd.DataFrame({
    "age": np.random.randint(20, 90, n_samples),
    "length_of_stay": np.random.randint(1, 15, n_samples),
    "num_lab_tests": np.random.randint(1, 30, n_samples),
    "num_procedures": np.random.randint(0, 10, n_samples),
    "has_chronic_disease": np.random.choice([0, 1], n_samples),
    "previous_admissions": np.random.randint(0, 6, n_samples),
})

risk_score = (
    0.04 * data["age"] +
    0.6 * data["length_of_stay"] +
    0.3 * data["previous_admissions"] +
    1.5 * data["has_chronic_disease"] +
    np.random.normal(0, 1, n_samples)
)

# Binary target (readmitted or not)
data["readmitted"] = (risk_score > 8).astype(int)


# Features / Target

X = data.drop("readmitted", axis=1)
y = data["readmitted"]


#  Train / Test split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


# Model training

model = LogisticRegression(
    penalty="l2",
    C=1.0,
    solver="liblinear",
    class_weight="balanced",
    max_iter=1000
)

model.fit(X_train, y_train)


# Prediction

y_pred = model.predict(X_test)


# Evaluation

print("Classification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=[0, 1])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Logistic Regression")
plt.savefig("result.png", dpi=300)
plt.show()
