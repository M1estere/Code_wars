def changer(s):
    s = s.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    vowels = "aeiou"

    temp_string = ""
    result_string = ""

    for char in s:
        if (char == "z"):
            temp_string += "a"
        elif ((char in alphabet) and (char != "z")):
            temp_string += str(alphabet[alphabet.index(char) + 1])
        else:
            temp_string += char

    for char in temp_string:
        if (char in vowels):
            result_string += char.upper()
        else:
            result_string += char

    return result_string