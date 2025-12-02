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

df["ShippingDays"] = (df["ShipDate"] - df["OrderDate"]).dt.days
mean_shipping_by_category = df.groupby("Category")["ShippingDays"].mean()
print(mean_shipping_by_category)



