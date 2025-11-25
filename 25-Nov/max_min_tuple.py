nums=(33,20,30,60,50)
max1=-1
min1=9999

for n in nums:
    if n>max1:
        max1=n

for n in nums:
    if n<min1:
        min1=n

print(max1,min1)