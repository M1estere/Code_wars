def alphabet_position(text):
    text = text.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    result = ""

    for char in text:
        if char in alphabet:
            result += str(alphabet.find(char) + 1)
            result += " "
        else:
            result += ""

    return result.strip()