
import pandas as pd


customers = pd.DataFrame({
    'customer_id': [1, 2, 3, 4],
    'name': ['Asha', 'Vikram', 'Neha', 'Rohit'],
    'email': ['asha@example.com', 'vikram@example.com', 'neha@example.com', 'rohit@example.com'],
    'city': ['Kolkata', 'Delhi', 'Mumbai', 'Pune']
})

orders = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105, 106],
    'customer_id': [1, 1, 2, 3, 3, 4],
    'order_date': pd.to_datetime(['2025-01-05', '2025-01-15', '2025-02-03', '2025-02-10', '2025-03-02', '2025-03-15']),
    'item': ['Phone', 'Case', 'Rice', 'Jeans', 'Milk', 'Headphones'],
    'category': ['Electronics', 'Accessories', 'Grocery', 'Clothing', 'Grocery', 'Electronics'],
    'price': [15000, 500, 60, 1500, 50, 2500],
    'quantity': [1, 2, 5, 2, 10, 1]
})
orders['order_amount'] = orders['price'] * orders['quantity']

combined = orders.merge(customers, on='customer_id', how='left')

report = (
    combined.groupby(['customer_id', 'name', 'email', 'city'])
            .agg(
                total_orders=('order_id', 'count'),
                total_spent=('order_amount', 'sum'),
                last_order_date=('order_date', 'max')
            )
            .reset_index()
            .sort_values('total_spent', ascending=False)
)

print("Combined (joined) data:")
print(combined)
print("\nCustomer-level report:")
print(report)

