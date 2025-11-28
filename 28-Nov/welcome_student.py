def generate_welcome_letter(student_name, course_name):
    letter = f"""
    Hello {student_name},

    Welcome to the {course_name} course!
    """
    filename = f"Welcome_{student_name.replace(' ', '_')}.txt"
    with open(filename, "w") as file:
        file.write(letter)

    print(f"Welcome letter generated and saved as {filename}")

generate_welcome_letter("Ankur", "Python week 1")
