list1=[1,2,2,2,3,7,2,7,5,5]
seen = set()
result = []

for item in list1:
    if item not in seen:
        seen.add(item)
        result.append(item)
print(result)
