import pandas as pd
df=pd.DataFrame({
    "Name": ["Aisha", "", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 20, 21, 24]
})

#write to JSON file

df.to_json("students.json", orient="records", indent=4)

print("JSON file created")


#Read to the same JSON File
df = pd.read_json("students.json")


print("JSON File read successfully")
print(df)

