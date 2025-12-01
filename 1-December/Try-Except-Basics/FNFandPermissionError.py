try:
    f=open("data.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Access denied")
finally:
    print("finally statement")