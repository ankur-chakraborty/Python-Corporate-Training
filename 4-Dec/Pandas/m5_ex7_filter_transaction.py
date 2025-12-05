
import pandas as pd

transactions = pd.DataFrame({
    'transaction_id': [1, 2, 3, 4, 5, 6],
    'customer_id': [1, 1, 2, 2, 3, 3],
    'date': pd.to_datetime(['2025-01-05', '2025-01-20', '2025-02-04', '2025-02-18', '2025-03-01', '2025-03-10']),
    'amount': [3000, 2500, 400, 100, 6000, 50]
})


totals = transactions.groupby('customer_id', as_index=False)['amount'].sum().rename(columns={'amount': 'total_spent'})

high_value_customers = totals[totals['total_spent'] > 5000]


filtered_transactions = transactions.merge(high_value_customers, on='customer_id', how='inner')

print("Total spend per customer:")
print(totals)
print("\nCustomers with total_spent > 5000:")
print(high_value_customers)
print("\nTransactions for high-value customers:")
print(filtered_transactions)
