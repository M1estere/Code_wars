def solve(s):
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    lower_counter = 0
    upper_counter = 0

    for char in s:
        if (char in lower_alphabet): lower_counter += 1
        if (char in upper_alphabet): upper_counter += 1

    return s.lower() if lower_counter >= upper_counter else s.upper()