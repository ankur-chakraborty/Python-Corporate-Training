import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

# print(df)
# print(df.head(2))
# print(df.tail(2))
# print(df.shape)
# print(df.columns)
# print(df.describe())


# print(df["Name"])
# print(df[["Marks","Name"]])
#
# high_sc=df[df["Marks"]>80]
# print(high_sc)
#
# filtered=df[(df["Marks"]>70) & (df["Age"]>22)]
# print(filtered)


# df["Result"]=df["Marks"].apply(lambda x:"Pass" if x>=60 else "Fail")
# print(df)


# sorted_df=df.sort_values("Marks", ascending=False)
# print(sorted_df)


# df2=df.copy()
# df2.loc[2,"City"]=None
# print(df2.isnull().sum())
#
# df2_filled=df2.fillna("Unknown")
# print(df2_filled)


# city_count=df.groupby("City")["Name"].count()
# print(city_count)
#
# avg_marks=df.groupby("City")["Marks"].mean()
# print(avg_marks)