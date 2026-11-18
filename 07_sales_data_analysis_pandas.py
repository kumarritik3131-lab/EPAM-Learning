# Sales data analysis using pandas.
# Install dependency: pip install pandas

import pandas as pd

data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Mouse", "Monitor"],
    "Category": ["Electronics", "Accessories", "Accessories",
                 "Electronics", "Accessories", "Electronics"],
    "Units_Sold": [3, 15, 8, 2, 10, 4],
    "Unit_Price": [55000, 500, 1200, 55000, 500, 9000]
}

df = pd.DataFrame(data)

# Create a calculated column.
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

print("\\nComplete sales data:")
print(df)

print("\\nBasic information:")
print(df.info())

print("\\nDescriptive statistics:")
print(df[["Units_Sold", "Unit_Price", "Revenue"]].describe())

print("\\nTotal revenue by product:")
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(
    ascending=False
)
print(product_revenue)

print("\\nRevenue by category:")
print(df.groupby("Category")["Revenue"].sum())

# Save the processed data for later use.
df.to_csv("sales_analysis_output.csv", index=False)
print("\\nSaved sales_analysis_output.csv")
