
def count_vowels_consonants_digits(text):
    vowels = "aeiouAEIOU"
    vowel_count = consonant_count = digit_count = 0

    for char in text:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Digits: {digit_count}")


string_input = input("Enter a string: ")
count_vowels_consonants_digits(string_input)
