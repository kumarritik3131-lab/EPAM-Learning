# Diabetes progression prediction using linear regression.
# Install dependencies: pip install pandas scikit-learn

import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load a built-in regression dataset.
diabetes = load_diabetes(as_frame=True)
df = diabetes.frame

print("Dataset preview:")
print(df.head())

print("\\nDataset dimensions:", df.shape)
print("\\nColumn names:")
print(df.columns.tolist())

# The target is a quantitative measure of disease progression.
X = df.drop(columns="target")
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\\nModel evaluation:")
print("Mean absolute error:", mean_absolute_error(y_test, predictions))
print("Mean squared error:", mean_squared_error(y_test, predictions))
print("R-squared:", r2_score(y_test, predictions))

# Compare a few actual and predicted values.
comparison = pd.DataFrame({
    "Actual": y_test.iloc[:10].values,
    "Predicted": predictions[:10]
})
print("\\nActual vs predicted values:")
print(comparison.round(2))

# Display the learned feature coefficients.
coefficients = pd.Series(model.coef_, index=X.columns)
print("\\nModel coefficients:")
print(coefficients.sort_values(ascending=False))
