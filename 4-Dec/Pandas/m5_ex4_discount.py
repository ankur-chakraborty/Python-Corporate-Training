
import pandas as pd


data = {
    'ProductID':        [1, 2, 3, 4, 5],
    'ProductCategory':  ['Electronics', 'Electronics', 'Clothing', 'Grocery', 'Clothing'],
    'Product':          ['Phone', 'Headphones', 'Jeans', 'Milk', 'T-Shirt'],
    'Price':            [15000.0, 2500.0, 1500.0, 50.0, 800.0]
}
df = pd.DataFrame(data)


df['DiscountedPrice'] = (df['Price'] * 0.90).round(2)

print("Input dataframe:")
print(df[['ProductID', 'ProductCategory', 'Product', 'Price']])
print("\nWith 10% DiscountedPrice:")
print(df[['ProductID', 'Product', 'Price', 'DiscountedPrice']])
