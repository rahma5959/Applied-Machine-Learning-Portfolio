import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree


# Data generation

np.random.seed(42)
n_samples = 1000

data = {
    'weight': np.random.normal(150, 30, n_samples),
    'size': np.random.normal(8, 2, n_samples),
    'color_intensity': np.random.uniform(0, 1, n_samples)
}

df = pd.DataFrame(data)

# Create labels (vectorized version)

conditions = [
    (df['weight'] > 180) & (df['size'] > 9),
    (df['weight'] < 120) & (df['size'] < 7)
]

choices = ['Apple', 'Orange']

df['label'] = np.select(conditions, choices, default='Unknown')


# Features and target

X = df[['weight', 'size', 'color_intensity']]
y = df['label']


# Train/test split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train Decision Tree

model = DecisionTreeClassifier(
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=3,
    random_state=42
)

model.fit(X_train, y_train)



# Model evaluation
print("Train accuracy:", model.score(X_train, y_train))
print("Test accuracy:", model.score(X_test, y_test))

print("\nClassification Report:\n")
print(classification_report(y_test, model.predict(X_test)))

print("Confusion Matrix:\n")
print(confusion_matrix(y_test, model.predict(X_test)))

# Visualize the tree

plt.figure(figsize=(12, 8))
plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True
)
plt.title("Decision Tree for Fruit Classification")
plt.tight_layout()
plt.savefig("result.png", dpi=300)
plt.show()
