data = (1, "apple", 3, "banana", 4, "cat")

numbers_tuple = tuple([x for x in data if isinstance(x, (int, float))])
strings_tuple = tuple([x for x in data if isinstance(x, str)])

print("Numbers:", numbers_tuple)
print("Strings:", strings_tuple)
