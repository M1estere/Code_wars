def calculator(txt):
    operand = 0

    if ("+" in txt):
        txt_list = txt.split("+")
        operand = 1
    if ("-" in txt):
        txt_list = txt.split("-")
        operand = 2
    if ("*" in txt):
        txt_list = txt.split("*")
        operand = 3
    if ("//" in txt):
        txt_list = txt.split("//")
        operand = 4

    left_dots = txt_list[0].count(".")
    right_dots = txt_list[1].count(".")

    if (operand == 1): return "." * (left_dots + right_dots)
    if (operand == 2): return "." * (left_dots - right_dots)
    if (operand == 3): return "." * (left_dots * right_dots)
    if (operand == 4): return "." * (left_dots // right_dots)