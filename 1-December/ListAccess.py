def list_acc(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of range. Valid range is 0 to {len(lst)-1}."

my_list = [10, 20, 30]
print(list_acc(my_list, 1))
print(list_acc(my_list, 5))
