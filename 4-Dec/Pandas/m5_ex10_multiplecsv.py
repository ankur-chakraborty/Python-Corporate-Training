
import pandas as pd

df1 = pd.DataFrame({
    'order_id': [101, 102, 103],
    'customer_id': [1, 1, 2],
    'amount': [15000, 1000, 300]
})

df2 = pd.DataFrame({
    'order_id': [103, 104, 105],   # 103 duplicates across files
    'customer_id': [2, 3, 3],
    'amount': [300, 6000, 50]
})

df3 = pd.DataFrame({
    'order_id': [106, 105, 107],   # 105 duplicates across files
    'customer_id': [4, 3, 2],
    'amount': [2500, 50, 400]
})

combined = pd.concat([df1, df2, df3], ignore_index=True)

final_df = combined.drop_duplicates(subset=['order_id'], keep='first')  # or keep='last'

print("Combined dataframe (before de-dup):")
print(combined)
print("\nFinal dataframe (deduplicated by order_id):")
print(final_df)

