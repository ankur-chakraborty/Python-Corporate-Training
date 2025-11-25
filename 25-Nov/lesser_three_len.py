lst = ["hi", "hello", "a", "world", "go", "yes"]
result = []
for s in lst:
    if len(s) >= 3:
        result.append(s)

print(result)
