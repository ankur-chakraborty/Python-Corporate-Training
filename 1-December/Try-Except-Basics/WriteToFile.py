def write_user_input_to_file(file_path):
    try:
        user_input = input("Enter some text to save in the file: ")
        file = open(file_path, 'w')
    except PermissionError:
        print(f"Error: Permission denied to write to '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        file.write(user_input)
        print(f"Successfully wrote to '{file_path}'.")
    finally:
        try:
            file.close()
        except NameError:
            pass
write_user_input_to_file("output.txt")
