def count_file_stats(filename):
    with open(filename, 'r') as file:
        text = file.read()
    char_count = len(text)
    word_count = len(text.split())
    with open(filename, 'r') as file:
        line_count = sum(1 for _ in file)

    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")

filename = "sample.txt"
count_file_stats(filename)
