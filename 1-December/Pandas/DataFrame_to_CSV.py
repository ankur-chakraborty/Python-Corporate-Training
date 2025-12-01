import pandas as pd

data = {
    "Name": ["Ankur", "Dipsu", "Messi"],
    "Marks":[85,92,78],
    "City":["Mumbai","Delhi","Chennai"]
}

df=pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("CSV file created")