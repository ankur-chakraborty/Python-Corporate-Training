
import pandas as pd
import numpy as np


products = ["Laptop", "Apple", "Mouse"]
categories = ["Electronics", "Grocery", "Electronics"]

data = {
    "OrderID": np.arange(1, 101),
    "ProductID": np.random.choice(products, 100),
    "Category": np.random.choice(categories, 100),
    "UnitPrice": np.random.randint(1000, 70000, 100),
    "Quantity": np.random.randint(1, 5, 100)
}

df = pd.DataFrame(data)


df.loc[0, "UnitPrice"] = np.nan
df.loc[1, "ProductID"] = np.nan


from pandas.api.types import is_numeric_dtype

for col in df.columns:
    if is_numeric_dtype(df[col]):
        df[col].fillna(df[col].median(), inplace=True)
    else:
        mode_vals = df[col].mode()
        df[col].fillna(mode_vals.iloc[0] if not mode_vals.empty else "Unknown", inplace=True)

print("Missing values after fill:\n", df.isna().sum())
