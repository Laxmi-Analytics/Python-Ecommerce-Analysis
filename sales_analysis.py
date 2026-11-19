import pandas as pd 
data={
    "Order_ID": list(range(101, 151)),
    "Product": [
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard",
        "Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"
    ],
    "Category": ["Electronics"] * 50,
    "Quantity": [
        2, 3, 1, 4, 2, 1, 2, 3, 2, 5,
        3, 1, 2, 3, 4, 2, 4, 1, 5, 2,
        1, 3, 2, 4, 3, 2, 1, 4, 3, 2,
        4, 2, 3, 1, 5, 2, 3, 2, 4, 1,
        3, 2, 1, 5, 2, 1, 4, 3, 2, 5
    ],
    "Unit_Price": [
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000,
        50000, 20000, 15000, 2000, 1000
    ],
    "Unit_Cost": [
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600,
        35000, 12000, 9000, 1200, 600
    ]
}
df=pd.DataFrame(data)
df["Total_Sales"]=df["Quantity"]*df["Unit_Price"]
total_sales=df["Total_Sales"].sum()
df["Profit_Per_Unit"]=df["Unit_Price"]-df["Unit_Cost"]
df["Total_Profit"]=df["Quantity"]*df["Profit_Per_Unit"]
total_profit=df["Total_Profit"].sum()
print(df)
print("Total Sales:",total_sales)
print("Total Profit:",total_profit)
product_sales=df.groupby("Product")["Total_Sales"].sum()
product_profit=df.groupby("Product")["Total_Profit"].sum()
highest_product=product_sales.idxmax()
print("Highest Selling Product:", highest_product)
comparison=pd.DataFrame({
    "Total Sales": product_sales,
    "Total Profit": product_profit
})
print("\nSales vs Profit Comparison:")
print(comparison)
product_margin=(
    df.groupby("Product")["Total_Profit"].sum()
    / df.groupby("Product")["Total_Sales"].sum()
) * 100
print("\nProduct-wise Profit Margin:")
print(product_margin.round(2))
import matplotlib.pyplot as plt
product_sales.plot(kind="bar",title="Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
product_profit.plot(kind="bar",title="Product-wise Profit")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.tight_layout()
plt.show()
product_margin.plot(kind="bar",title="Product-wise Profit Margin")
plt.xlabel("Product")
plt.ylabel("Profit Margin (%)")
plt.tight_layout()
plt.show()
