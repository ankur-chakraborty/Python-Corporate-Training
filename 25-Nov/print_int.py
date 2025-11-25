data = (10, (20, 30), (40, (50, 60)))
def print_integers(t):
    for item in t:
        if isinstance(item, int):
            print(item)
        elif isinstance(item, tuple):
            print_integers(item)
print_integers(data)
