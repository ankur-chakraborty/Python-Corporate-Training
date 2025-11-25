nums = [5, 2, 7, 5, 9, 5, 3]
length=len(nums)
x=5
list1=[]
for i in range (0,length):
    if x==nums[i]:
        list1.append(i)

print(list1)