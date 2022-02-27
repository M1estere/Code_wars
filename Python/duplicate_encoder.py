def duplicate_encode(word):

    result_string = ""

    for char in word.lower():
        if (word.lower().count(char) == 1):
            result_string = result_string + "("
        else:
            result_string = result_string + ")"

    return result_string