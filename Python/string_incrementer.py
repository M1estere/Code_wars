def increment_string(s):

    stripped_chars = s.rstrip('1234567890')
    digits = s[len(stripped_chars):]
    if len(digits) == 0:
        return s + '1'
    else:
        length = len(digits)

        new_digits = 1 + int(digits)
        new_digits = str(new_digits).zfill(length)

        return stripped_chars + new_digits