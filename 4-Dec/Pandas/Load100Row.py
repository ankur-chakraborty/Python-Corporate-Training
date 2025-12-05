import pandas as pd
RETAIL_CSV = "retail_100.csv"
CUSTOMERS_CSV = "customers.csv"
ORDERS_CSV = "orders.csv"
CUSTOMERS_JSON = "customers.json"
df = pd.read_csv(RETAIL_CSV, parse_dates=["order_date"])


total_orders = df["order_id"].nunique()



#Q30
# if "revenue" not in df.columns:
#     df["revenue"] = df["price"] * df["quantity"]
# total_revenue = df["revenue"].sum()
# top_5_products = (
#     df.groupby("product", as_index=False)["revenue"]
#       .sum()
#       .sort_values(by="revenue", ascending=False)
#       .head(5)
# )
#
# print("Total Orders:", total_orders)
# print("Total Revenue:", total_revenue)
# print("Top 5 Products:\n", top_5_products)





#Q31

print("Missing values per column:\n", df.isna().sum())

# Fill numeric with median
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].apply(lambda col: col.fillna(col.median()))


