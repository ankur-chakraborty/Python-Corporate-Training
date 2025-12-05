def flatten(nested):
    return [item for sub in nested for item in sub]

nested = [[1, 2], [3, 4], [5, 6]]
print(flatten(nested))
