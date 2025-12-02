import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, None, 78, None, 55],
    "City": ["Mumbai", "Delhi", None, "Bangalore", None],
    "Age": [22, 25, None, 21, 24]
})

print(df.isnull())
print(df.isnull().sum())


print(df.replace("",None).isnull().sum())