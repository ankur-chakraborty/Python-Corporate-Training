student={
    "name":"Ankur",
    "age":22,
    "city":"Kolkata"
}

print(student["name"])

print(student.get("age"))
print(student.get("city")) #2 types of approach to get

student["email"]="akc@gmail.com"

student["city"]="Hyderabad"

for k in student.keys():
    print(k)
for v in student.values():
    print(v)
for k,v in student.items():
    print(k,v)



student.pop("city")

del student["age"]
student.clear()