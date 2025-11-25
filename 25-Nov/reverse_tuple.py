s1= ("python", "cloud", "data")
list1 = []
for word in s1:
    list1.append(word[::-1])
rtuple = tuple(list1)
print(rtuple)
