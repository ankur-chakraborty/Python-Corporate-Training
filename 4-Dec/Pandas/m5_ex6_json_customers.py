
import pandas as pd


customers_json = [
    {
        "customer_id": 1,
        "name": "Asha",
        "email": "asha@example.com",
        "address": {"street": "MG Road", "city": "Kolkata", "zip": "700001"},
        "preferences": {"newsletter": True, "sms": False},
        "orders": [
            {"order_id": 101, "date": "2025-01-05", "amount": 15000},
            {"order_id": 102, "date": "2025-01-15", "amount": 1000}
        ]
    },
    {
        "customer_id": 2,
        "name": "Vikram",
        "email": "vikram@example.com",
        "address": {"street": "Ring Rd", "city": "Delhi", "zip": "110001"},
        "preferences": {"newsletter": False, "sms": True},
        "orders": [
            {"order_id": 103, "date": "2025-02-03", "amount": 300},
        ]
    }
]


flat_customers = pd.json_normalize(customers_json, sep='_')
print("Flattened customers (dict fields normalized):")
print(flat_customers)

orders_norm = pd.json_normalize(
    customers_json,
    record_path='orders',
    meta=['customer_id', 'name', 'email'],
    sep='_'
)

orders_norm['date'] = pd.to_datetime(orders_norm['date'])

print("\nNormalized orders with customer meta:")
print(orders_norm)

