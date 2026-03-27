
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report


# Data generation 

np.random.seed(42)
n_samples = 1000

data = pd.DataFrame({
    "age": np.random.randint(18, 70, n_samples),
    "gender": np.random.choice([0, 1], n_samples),  # 0=female, 1=male
    "time_on_site": np.random.normal(5, 2, n_samples),  # minutes
    "pages_viewed": np.random.randint(1, 20, n_samples),
    "previous_purchases": np.random.randint(0, 10, n_samples),
})

data["buy"] = ((data["time_on_site"] * 0.3 +
                data["pages_viewed"] * 0.5 +
                data["previous_purchases"] * 1.0 +
                np.random.randn(n_samples)) > 8).astype(int)


# Train/Test Split

X = data.drop("buy", axis=1)
y = data["buy"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train Random Forest Model

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)


# Evaluate Model

y_pred = model.predict(X_test)

print("Classification Report:")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=[0,1])
disp.plot(cmap=plt.cm.Blues)
plt.title("Confusion Matrix - Random Forest")
plt.savefig("result.png", dpi=300)
plt.show()
