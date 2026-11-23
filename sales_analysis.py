import pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV File
df = pd.read_csv("sales_data.csv")

print("--- E-COMMERCE SALES ANALYSIS ---")

# 2. Data Quality Check
print("\n--- Data Quality Check ---")

print("Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# 3. Data Cleaning
df = df.drop_duplicates()
df = df.dropna()

print("\nCleaned Dataset Shape:", df.shape)

# 4. Calculate Sales and Profit
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

df["Profit_Per_Unit"] = (
    df["Unit_Price"] - df["Unit_Cost"]
)

df["Total_Profit"] = (
    df["Quantity"] * df["Profit_Per_Unit"]
)

# 5. Overall Business Summary
total_sales = df["Total_Sales"].sum()
total_profit = df["Total_Profit"].sum()

print("\n--- Business Summary ---")
print("Total Sales: ₹", total_sales)
print("Total Profit: ₹", total_profit)

# 6. Product-wise Analysis
product_analysis = df.groupby("Product").agg(
    Total_Sales=("Total_Sales", "sum"),
    Total_Profit=("Total_Profit", "sum"),
    Total_Quantity=("Quantity", "sum")
)

product_analysis["Profit_Margin"] = (
    product_analysis["Total_Profit"]
    / product_analysis["Total_Sales"] * 100
)

print("\n--- Product-wise Analysis ---")
print(product_analysis)

# 7. Advanced Business Insights
highest_revenue = product_analysis["Total_Sales"].idxmax()
highest_profit = product_analysis["Total_Profit"].idxmax()
best_selling = product_analysis["Total_Quantity"].idxmax()

print("\n--- Business Insights ---")
print("Highest Revenue Product:", highest_revenue)
print("Highest Profit Product:", highest_profit)
print("Best Selling Product:", best_selling)

# 8. Product-wise Sales Chart
product_analysis["Total_Sales"].plot(
    kind="bar",
    title="Product-wise Sales",
    xlabel="Product",
    ylabel="Sales (₹)",
    figsize=(9, 5)
)

plt.tight_layout()
plt.savefig("Product_Wise_Sales_Chart.png")
plt.show()

# 9. Product-wise Profit Chart
product_analysis["Total_Profit"].plot(
    kind="bar",
    title="Product-wise Profit",
    xlabel="Product",
    ylabel="Profit (₹)",
    figsize=(9, 5)
)

plt.tight_layout()
plt.savefig("Product_Wise_Profit_Chart.png")
plt.show()

# 10. Product-wise Profit Margin Chart
product_analysis["Profit_Margin"].plot(
    kind="bar",
    title="Product-wise Profit Margin",
    xlabel="Product",
    ylabel="Profit Margin (%)",
    figsize=(9, 5)
)

plt.tight_layout()
plt.savefig("Product_Wise_Profit_Margin_Chart.png")
plt.show()

print("\nAnalysis Completed Successfully!")
