nums = [10, 3, 5, 12, 8, 7, 1]
even=[]
odd=[]

for n in nums:
    if n%2==0:
        even.append(n)
    else:
        odd.append(n)

print(odd)
print(even)