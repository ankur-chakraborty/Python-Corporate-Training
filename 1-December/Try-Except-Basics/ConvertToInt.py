def convert_to_int(lst):
    result = []
    for item in lst:
        try:
            result.append(int(item))
        except ValueError:
            print(f"Warning: Cannot convert '{item}' to integer.")
    return result
data = ["10", "20", "abc", "30.5", "", "40"]
converted = convert_to_int(data)
print("Converted list:", converted)
