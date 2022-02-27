def vowel_indices(word):
    word = word.lower()

    vowels = ["a", "e", "i", "o", "u", "y"]

    result_list = []

    for i, j in enumerate(word):
        if j in vowels or j in [k for k in vowels]:
            result_list.append(i + 1)

    return result_list