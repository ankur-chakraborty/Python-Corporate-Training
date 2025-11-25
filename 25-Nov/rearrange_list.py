list1=[1,-9,6,-2,7,9,-5]
list2=[]
list3=[]

for n in list1:
    if n>0:
        list2.append(n)
    else:
        list3.append(n)

for n in list2:
    list3.append(n)
print(list3)