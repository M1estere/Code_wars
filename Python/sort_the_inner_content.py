def sort_the_inner_content(words):
    temp_list = []
    words_list = words.split()
    for word in words_list:
        if (len(word) == 1):
            temp_list.append("".join(word))
        else:
            first_item = list(word[0])
            middle_item = sorted(list(word[1:-1]), reverse=True)
            last_item = list(word[-1])

            temp_list.append("".join(first_item + middle_item + last_item))

    return " ".join(temp_list)