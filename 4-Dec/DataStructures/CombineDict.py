def combine_sum_values(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        if k in result and isinstance(result[k], (int, float)) and isinstance(v, (int, float)):
            result[k] += v
        else:
            result[k] = v
    return result
a = {"apples": 10, "bananas": 5, "oranges": 7}
b = {"bananas": 2, "oranges": 3, "grapes": 4}
print(combine_sum_values(a, b))
