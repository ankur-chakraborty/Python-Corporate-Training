def merge_lists_to_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError("Different lengths")
    return dict(zip(keys, values))

list1 = ["id", "name", "price"]
list2 = [101, "Adapter", 499]
print(merge_lists_to_dict(list1, list2))
