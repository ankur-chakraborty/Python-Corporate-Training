set1={1,2,3}
set2={3,4,5,6}

flag=True

for item in set1:
    if item in set2:
        flag=False

if flag:
    print("Disjoint set")
else:
    print("Not disjoint set")