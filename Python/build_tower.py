def tower_builder(floors):

    result_list = []
    line_width = (floors * 2) - 1

    for i in range(1, 2 * floors, 2):
        stars = "*" * i
        line = stars.center(line_width)
        result_list.append(line)

    return result_list