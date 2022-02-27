def is_isogram(string):
    string = string.lower()
    word_alphabet = ""

    word_arr = list(string)

    for letter in word_arr:
        word_alphabet += letter

    for char in word_alphabet:
        if (word_alphabet.count(char) > 1):
            return False
    return True


print(is_isogram(str(input())))