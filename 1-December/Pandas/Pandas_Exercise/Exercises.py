import pandas as pd




df=pd.read_csv("sales_data.csv")


# Exercise 1
# print(df.head(5))
# print(df.tail(5))
# print(df.columns)
# print(df.shape)



# Exercise 2

# df['Date'] = pd.to_datetime(df['Date'])
#
# df['Year'] = df['Date'].dt.year
# df['Month'] = df['Date'].dt.month
# df['Day'] = df['Date'].dt.day
# df.to_csv('sales_data_updated.csv', index=False)



# Exercise 3

# total_sales=df.groupby("Store")["TotalPrice"].sum()
# print(total_sales)
#
# total_sales2=df.groupby("City")["TotalPrice"].sum()
# print(total_sales2)
#
# total_sales3=df.groupby("Category")["TotalPrice"].sum()
# print(total_sales3)




# Exercise 4

# sorted_a=df.sort_values("TotalPrice", ascending=True)
# print(sorted_a.head(5))




# Exercise 5

# filtered=df[(df["Category"]>"Electronics") & (df["Quantity"]>1)]
# print(filtered)




# Exercise 6

# df['Discount'] = df['CustomerType'].apply(lambda x: 0.10 if x == 'Returning' else 0.05)
# df['FinalPrice'] = df['TotalPrice'] * (1 - df['Discount'])
# df.to_csv('sales_data_with_discount.csv', index=False)
#
# print(df.head(10))





# Exercise 7

# payment_counts = df['PaymentMethod'].value_counts()
#
# cash_count = payment_counts.get('Cash', 0)
# credit_card_count = payment_counts.get('Credit Card', 0)
# upi_count = payment_counts.get('UPI', 0)
#
# print(f"Cash: {cash_count}")
# print(f"Credit Card: {credit_card_count}")
# print(f"UPI: {upi_count}")




# Exercise 8

# df['Revenue'] = df['TotalPrice'] * df['Quantity']
# grouped_df = df.groupby('Category').agg(
#     Total_Quantity=('Quantity', 'sum'),
#     Total_Revenue=('Revenue', 'sum')
# ).reset_index()
#
# grouped_df.to_csv('category_summary.csv', index=False)
#
# print(grouped_df)





# Exercise 9

#
# store_sales = df.groupby('Store')['TotalPrice'].sum().reset_index()
#
# top_store = store_sales.loc[store_sales['TotalPrice'].idxmax()]
#
# print("Store with highest total sales:")
# print(f"{top_store['Store']} - Total Sales: {top_store['TotalPrice']}")




# Exercise 10

# filtered_df = df[df['Product'].str.contains('a', case=False, na=False)]
# filtered_df.to_csv('products_with_a.csv', index=False)
# print(filtered_df.head())



# Exercise 11

# df['Date'] = pd.to_datetime(df['Date'])
# sorted_df = df.sort_values(by=['Date', 'TotalPrice'], ascending=[True, False])
# sorted_df.to_csv('sales_data_sorted.csv', index=False)
# print(sorted_df.head())


# Exercise 12

# avg_revenue = df.groupby('CustomerType')['TotalPrice'].mean().reset_index()
# avg_revenue.columns = ['CustomerType', 'Avg_Revenue_Per_Order']
# print("Average Revenue per Order by CustomerType:")
# print(avg_revenue)


# Exercise 13

# pivot_table = pd.pivot_table(
#     df,
#     values='TotalPrice',
#     index='Category',
#     columns='PaymentMethod',
#     aggfunc='sum',
#     fill_value=0
# )
#
# print("Pivot Table (Category vs PaymentMethod):")
# print(pivot_table)
# pivot_table.to_csv("pivot_category_payment.csv")
# print("Pivot table saved to pivot_category_payment.csv")


# Exercise 14

# electronics_df = df[df['Category'] == 'Electronics']
# electronics_df.to_csv("electronics_only.csv", index=False)
# print("Electronics-only dataset saved to electronics_only.csv")

# Exercise 15


final_df = (
    df[df['Quantity'] >= 2]
    .query("Category == 'Apparel'")
    .assign(TotalValue=lambda x: x['Quantity'] * x['UnitPrice'])
    .sort_values(by='TotalValue', ascending=False)
    .reset_index(drop=True)  # Reset index
)

print("Final DataFrame:")
print(final_df)

final_df.to_csv("apparel_filtered_sorted.csv", index=False)
print("Final DataFrame saved to apparel_filtered_sorted.csv")