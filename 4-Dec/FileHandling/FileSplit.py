def split_file(input_file, first_half_file, second_half_file):

    with open(input_file, 'r') as file:
        lines = file.readlines()

    mid = len(lines) // 2

    with open(first_half_file, 'w') as f1:
        f1.writelines(lines[:mid])

    with open(second_half_file, 'w') as f2:
        f2.writelines(lines[mid:])

    print(f"File split completed:\nFirst half -> {first_half_file}\nSecond half -> {second_half_file}")

split_file("sample.txt", "first_half.txt", "second_half.txt")
