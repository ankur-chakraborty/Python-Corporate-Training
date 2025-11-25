lst = [1, 2, 3, 4, 5]
n = 2
n = n % len(lst)

for i in range(n):
    first = lst[0]
    for j in range(len(lst) - 1):
        lst[j] = lst[j + 1]
    lst[-1] = first
print(lst)
