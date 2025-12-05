
import pandas as pd

data = {
    'OrderID':      [101, 101, 102, 103, 103, 104],
    'ProductCategory': ['Electronics', 'Electronics', 'Grocery', 'Clothing', 'Clothing', 'Grocery'],
    'Product':      ['Phone', 'Headphones', 'Rice', 'T-Shirt', 'Jeans', 'Milk'],
    'Price':        [15000.0, 2500.0, 60.0, 800.0, 1500.0, 50.0],  # unit price
    'Quantity':     [1, 2, 5, 3, 2, 10]
}
df = pd.DataFrame(data)


df['Sales'] = df['Price'] * df['Quantity']

summary = (
    df.groupby('ProductCategory')
      .agg(
          TotalSales=('Sales', 'sum'),
          OrderCount=('OrderID', 'nunique'),   # distinct orders per category
          AvgPrice=('Price', 'mean')           # average unit price
      )
      .reset_index()
)

print("Input dataframe:")
print(df)
print("\nGrouped summary by ProductCategory:")
print(summary)
