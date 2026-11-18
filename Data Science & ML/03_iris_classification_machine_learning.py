# Iris flower classification using pandas and scikit-learn.
# Install dependencies: pip install pandas scikit-learn

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load the built-in Iris dataset.
iris = load_iris(as_frame=True)
df = iris.frame

print("First five rows:")
print(df.head())

print("\\nDataset shape:", df.shape)
print("\\nMissing values:")
print(df.isnull().sum())

# Separate features (X) and target labels (y).
X = df[iris.feature_names]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Scaling is fitted only on training data inside the pipeline.
model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("\\nAccuracy:", accuracy_score(y_test, predictions))
print("\\nClassification report:")
print(classification_report(
    y_test, predictions, target_names=iris.target_names
))

# Predict the species for one new flower measurement.
new_flower = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=iris.feature_names
)
predicted_class = model.predict(new_flower)[0]
print("Predicted species:", iris.target_names[predicted_class])
