import pandas as pd

df=pd.read_csv("NewData.csv")
#A Set

# print(df.head(10))
#
# print(df.shape)
#
# print(df.info())
# print(df.describe())
#
# print(df.isnull().sum())
#
#
# df['OrderDate'] = pd.to_datetime(df['OrderDate'])
# df['ShipDate'] = pd.to_datetime(df['ShipDate'])
#
# df.to_csv('orders_clean.csv', index=False)





#B Set


# df['OrderDate'] = pd.to_datetime(df['OrderDate'])
# df['ShipDate'] = pd.to_datetime(df['ShipDate'])
#
# df['ShippingDays'] = (df['ShipDate'] - df['OrderDate']).dt.days
#
# df['ProfitMargin'] = df['Profit'] / df['Sales']



# f = pd.DataFrame(df)
# df['CustomerName'] = df['CustomerName'].str.title()
#
#
# print(df)




# df = df[df['Sales'] > 0]
#
# print(df)


# df['Discount'] = (df['Discount'] * 100).round(2).astype(str) + '%'
#
# print(df)




 #C Set


# west_orders = df[df["Region"] == "West"]
# print(west_orders)
#
# tech_sales_400 = df[(df["Category"] == "Technology") & (df["Sales"] > 400)]
# print(tech_sales_400)
#
# returned_products = df[df["Category"] == "Yes"]
# print(returned_products)
#
# furniture_after_date = df[(df["Category"] == "Furniture") & (df["ShipDate"] > "2024-01-20")]
# print(furniture_after_date)
#
# low_profit_orders = df[df["Profit"] < 200]
# print(low_profit_orders)






#D set


# sorted_sales_desc = df.sort_values("Sales", ascending=False)
# print(sorted_sales_desc)
#
# sorted_profit_margin = df.sort_values("Profit")
# print(sorted_profit_margin)
#
# sorted_region_city = df.sort_values(by=["Region", "City"])
# print(sorted_region_city)
#
# sorted_shipping_days = df.sort_values("ShipDate", ascending=False)
# print(sorted_shipping_days)
#
# sorted_customer_name = df.sort_values("CustomerName")
# print(sorted_customer_name)



#E Set

#
# sales_per_region = df.groupby("Region")["Sales"].sum()
# print(sales_per_region)
#
# avg_profit_category = df.groupby("Category")["Profit"].mean()
# print(avg_profit_category)
#
# orders_per_customer = df.groupby("CustomerName")["OrderID"].count()
# print(orders_per_customer)
#
# sales_per_segment = df.groupby("Segment")["Sales"].sum()
# print(sales_per_segment)
#
# qty_per_subcategory = df.groupby("SubCategory")["Quantity"].sum()
# print(qty_per_subcategory)
#
# df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors='coerce')
# df["ShipDate"] = pd.to_datetime(df["ShipDate"], errors='coerce')

# df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
# mean_shipping_by_category = df.groupby("Category")["ShippingDays"].mean()
# print(mean_shipping_by_category)




#F Set


# pivot = pd.pivot_table(
#     df,
#     index='Region',
#     columns='Category',
#     values='Sales',
#     aggfunc='sum',
#     fill_value=0
# )
# print(pivot)

# pivot = pd.pivot_table(
#     df,
#     index='SubCategory',
#     columns='Segment',
#     values='Profit',
#     aggfunc='sum',
# )
#
# print(pivot)



# pivot = pd.pivot_table(
#     df,
#     index='Region',
#     columns='Returned',
#     values='OrderID',
#     aggfunc='count',
#     fill_value=0
# )
#
# print(pivot)




# pivot = pd.pivot_table(
#     df,
#     index='Category',
#     values='UnitPrice',
#     aggfunc='mean'
# )
#
# print(pivot)




# pivot = pd.pivot_table(
#     df,
#     index='Month',
#     columns='Region',
#     values='Quantity',
#     aggfunc='sum',
#     fill_value=0
# )
#
# print(pivot)




#G set

# discount_df = pd.DataFrame({
#     'Segment': ['Consumer', 'Corporate', 'Home Office'],
#     'DiscountPct': [5, 8, 10]
# })
#
# df = df.merge(discount_df, on='Segment', how='left')
# print(df)




# tax_lookup = {
#     'East': 12,
#     'West': 10,
#     'South': 8,
#     'Central': 9
# }
#
# # Add TaxPct column
# df['TaxPct'] = df['Region'].map(tax_lookup)
#
# print(df)



# customer_totals = df.groupby('CustomerName').agg({
#     'Sales': 'sum',
#     'Profit': 'sum',
#     'Quantity': 'sum'
# }).reset_index()
# customer_totals.rename(columns={
#     'Sales': 'TotalSales',
#     'Profit': 'TotalProfit',
#     'Quantity': 'TotalQuantity'
# }, inplace=True)
#
# df = df.merge(customer_totals, on='CustomerName', how='left')
# print(df)





# product_summary = df.groupby('ProductName').agg({
#     'Sales': 'sum',
#     'Profit': 'sum'
# }).reset_index()
# product_summary['ProfitMargin'] = (product_summary['Profit'] / product_summary['Sales']).round(2)
# product_summary.rename(columns={
#     'Sales': 'TotalSales',
#     'Profit': 'TotalProfit'
# }, inplace=True)
#
# print(product_summary)



#H Set


# df['OrderDate'] = pd.to_datetime(df['OrderDate'])
#
# df['OrderYear'] = df['OrderDate'].dt.year
# df['OrderMonth'] = df['OrderDate'].dt.month
# df['OrderDay'] = df['OrderDate'].dt.day
#
# print(df)







# df['OrderDate'] = pd.to_datetime(df['OrderDate'])
# df['OrderDayOfWeek'] = df['OrderDate'].dt.day_name()
#
# print(df)







# df['OrderDate'] = pd.to_datetime(df['OrderDate'])
# df['ShipDate'] = pd.to_datetime(df['ShipDate'])
#
# # Calculate ShippingDays
# df['ShippingDays'] = (df['ShipDate'] - df['OrderDate']).dt.days
#
# # Filter orders shipped in more than 5 days
# delayed_orders = df[df['ShippingDays'] > 5]
#
# print(delayed_orders)






# df['OrderDate'] = pd.to_datetime(df['OrderDate'])
#
# df['YearMonth'] = df['OrderDate'].dt.to_period('M')  # e.g., 2025-01, 2025-02
#
# monthly_sales = df.groupby('YearMonth')['Sales'].sum().reset_index()
#
# print(monthly_sales)
