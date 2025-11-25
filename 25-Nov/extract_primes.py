nums = [10, 11, 12, 13, 17, 20, 23]
list1=[]
index=0
for n in nums:
    for i in range (2,n//2):
        if n%i==0:
            break
        else:
            list1.append(n)
            index += 1
            break

print(list1)
