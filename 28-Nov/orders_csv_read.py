import pandas as pd

orders = pd.read_csv('orders.csv')

orders['total_price'] = orders['quantity'] * orders['price']

final_total = orders['total_price'].sum()
final_row = pd.DataFrame([{'item': 'TOTAL', 'quantity': '', 'price': '', 'total_price': final_total}])

invoice.to_csv('invoice.csv', index=False)

print("Invoice generated successfully as 'invoice.csv'.")