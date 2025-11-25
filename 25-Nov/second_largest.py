nums = [23, 89, 12, 78, 55, 42]

max1=-1

for n in nums:
    if n>max1:
        max1=n

max2=-1
for n1 in nums:
    if n1!=max1:
        if n1>max2:
            max2=n1

print(max2)