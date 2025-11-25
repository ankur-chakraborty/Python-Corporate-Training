lst = [1, 2, 3, 2, 4, 1, 5, 1]
duplicates = []
for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)
