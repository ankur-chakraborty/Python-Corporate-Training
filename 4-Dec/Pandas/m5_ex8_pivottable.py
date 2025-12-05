
import pandas as pd

sales = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106],
    'category': ['Electronics', 'Accessories', 'Grocery', 'Clothing', 'Grocery', 'Electronics'],
    'date': pd.to_datetime(['2025-01-05', '2025-01-18', '2025-02-03', '2025-02-10', '2025-03-02', '2025-03-15']),
    'price': [15000, 500, 60, 1500, 50, 2500],
    'quantity': [1, 2, 5, 2, 10, 1]
})

sales['Sales'] = sales['price'] * sales['quantity']
sales['Month'] = sales['date'].dt.to_period('M').astype(str)  # e.g., '2025-01', '2025-02'

pivot = pd.pivot_table(
    sales,
    values='Sales',
    index='category',
    columns='Month',
    aggfunc='sum',
    fill_value=0
).sort_index()

print("Sales pivot (category x month):")
print(pivot)
