def accum(string):
    string = string.lower()

    counter = 0
    new_string = ""

    for char in string: # abc
        counter += 1
        new_string = new_string + char.upper()
        for i in range(counter - 1):
            new_string = new_string + char.lower()
        if (counter < len(string)): new_string += '-'

    return new_string