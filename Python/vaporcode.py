def vaporcode(s):
    s = s.replace(" ", "")
    s_list = list(s)

    result = ""

    for el in s_list:
        result += el.upper() + "  "

    return result.strip()


print(vaporcode("Lets go to the movies"))