nums={10,20,30,40}

#sets

data={1,2,2,3,3,3}
print(data)

s2={10,20,30}
empty=set()

#add ops
s={1,2,3}
s.add(4)
print(s)
s.update([5,6])
print(s)

#remove
s.remove(3)
s.discard(10)

print(s)


n1={1,2,3}
n2={3,4,5}

print(n1|n2) #union

print(n1&n2) #intersection

print(n1-n2) #{1,2}

print(n1^n2) #Symmetric difference - uncommon inputs {1,2,4,5}


print(4 in n2) #True

for item in n2:
    print(item)

repeat=[1,2,2,4,4,6,7,8]
unique=list(set(repeat))

print(unique)