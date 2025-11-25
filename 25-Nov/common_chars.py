words = ["python", "cloud", "data"]

unique_chars = set()

for word in words:
    for char in word:
        unique_chars.add(char)

print(unique_chars)
