set1={2,4,6,8,10}
target=12

for x in set1:
    for y in set1:
        if x<=y and x+y==target:
            print("(",x,",",y,")")

