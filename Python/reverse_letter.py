def reverse_letter(string):
    string = string.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    temp_string = ""

    for char in string:
        if (char in alphabet):
            temp_string = char + temp_string
        else:
            continue

    return temp_string
