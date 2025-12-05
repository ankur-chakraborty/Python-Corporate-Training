def word_frequency(sentence):
    words = sentence.split()
    freq_dict = {}
    for word in words:
        word = word.lower()
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict

sentence_input = input("Enter a sentence: ")
print(word_frequency(sentence_input))
