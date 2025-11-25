nums=[0, 3, 0, 5, 7, 0, 9]
length = len(nums)
final=[0]*length
index=0
for i in range (0,length):
    if nums[i]!=0:
        final[index]=nums[i]
        index+=1


nums=final

print(nums)