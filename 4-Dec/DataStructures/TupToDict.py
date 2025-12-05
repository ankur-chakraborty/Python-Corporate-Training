def tuples_to_dict_if_unique(pairs):
    keys = [k for k, _ in pairs]
    if len(set(keys)) != len(keys):
        return None
    return dict(pairs)
pairs_ok = [("id", 1), ("name", "Pen"), ("price", 10)]
pairs_dup = [("id", 1), ("name", "Pen"), ("id", 2)]
print(tuples_to_dict_if_unique(pairs_ok))
print(tuples_to_dict_if_unique(pairs_dup))
