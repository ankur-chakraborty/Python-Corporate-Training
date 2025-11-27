import csv
#Ex1
with open("notes.txt","w") as f:
    f.write("I am Ankur.\n")
    f.write("I am 22 years old.\n")
    f.write("I am a graduate from Amity University Kolkata in Computer Science and Engineering\n")
    f.write("Currently I am working at EY as a ASE.\n")
    f.write("I love cars.\n")



#Ex2
with open("notes.txt","a") as f:
    f.write("Appended line to notes.txt\n")



#Ex3
with open("notes.txt","r") as f:
    content=f.read()
    print(content)



#Ex4
with open("notes.txt", 'r') as f:
    lines = len(f.readlines())
    print('Total Number of lines:', lines)




#Ex5
with open("notes.txt", 'r') as f:
    content = f.read()
    words = content.split()
    word_count = len(words)



#Ex6
with open('notes.txt', 'r') as main, open('copy.txt', 'w') as copy:
    content = main.read()
    copy.write(content)



#Ex7
with open("notes.txt", 'r') as f:
    lines=f.readlines()
    for line in lines:
        if "Amity University" in line:
            print(line)



#Ex8
# with open('students.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader, None)
#     for row in csv_reader:
#         name, marks = row[0], row[1]
#         print(f"Name: {name}, Marks: {marks}")


#Ex9
with open("squares.txt","w") as f:
    for i in range (1,11):
        f.write(str(i**2)+"\n")
