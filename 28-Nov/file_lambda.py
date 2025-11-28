generate_line = lambda user: f"Hello {user}, welcome to Python training."

def write_dynamic_line(user, filename):
    with open(filename,"w") as f:
        f.write(generate_line(user))

write_dynamic_line("Ankur","welcome.txt")