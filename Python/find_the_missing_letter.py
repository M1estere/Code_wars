def find_missing_letter(chars):
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

    main_string = ""

    alphabet = ""

    for s in chars:
        main_string += s

    if (alphabet_upper.count(main_string[0]) != 0):
        alphabet = alphabet_upper
    else:
        alphabet = alphabet_lower

    start_index = alphabet.find(main_string[0])

    for i in range(start_index, len(main_string) + start_index):
        if ((main_string[i - start_index] == alphabet[i]) and (main_string[i - start_index + 1] == alphabet[i + 1])):
            continue
        else:
            return alphabet[i + 1]