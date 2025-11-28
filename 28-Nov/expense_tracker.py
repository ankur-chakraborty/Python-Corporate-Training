def get_expense(name, amount, list1):
    list1.append([name, amount])
    return list1


l1=[]
get_expense("Petrol", 5000, l1)
get_expense("Gym", 625, l1)
get_expense("Protein Shake", 2000, l1)
get_expense("Misc", 5000, l1)
get_expense("Car Parts", 10000, l1)

with open("expense_tracker.txt", "a") as file:
    for item in l1:
        file.write(item[0]+" "+str(item[1])+"\n")




