num=int(input("enter:"))

new=0
while num!=0:
    x=num%10
    num=num//10
    new=new*10+x
print(new)