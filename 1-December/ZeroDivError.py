a=int(input("enter a:"))
b=int(input("enter b:"))

try:
    x=a/b
except ZeroDivisionError:
    print("ZeroDivisionError")