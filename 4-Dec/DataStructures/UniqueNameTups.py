def unique_names(names_tuple):
    return tuple(dict.fromkeys(names_tuple))

names = ("Riya", "Aman", "Riya", "Kabir", "Aman")
print(unique_names(names)) 
