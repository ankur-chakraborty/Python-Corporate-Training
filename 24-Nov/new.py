names=["Ankur", "Ayushi", "Sriparna"]
numbers=[16, 6, 10]
mixed=["hi", 10, "messi", 5.6]

print(numbers)

print(names[-1])
print(mixed[3])


names.insert(1, "Tuneer")
names.append("Sam")

names.remove("Sam")
names.pop(2) #index pop
names.pop() #last element pop
del names[0]