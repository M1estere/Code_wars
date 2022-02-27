def solution(s):
    main_list = []
    result_string = ""

    if len(s) % 2 != 0:
        s += "_"

    for i in range(0, len(s), 2):
        main_list.append(s[i: i + 2])

    return main_list