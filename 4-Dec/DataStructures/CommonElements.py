def common_elements(set1, set2, set3):
    return set1 & set2 & set3

s1 = {1, 2, 3, 4}
s2 = {2, 3, 5}
s3 = {0, 2, 3, 6}
print(common_elements(s1, s2, s3))