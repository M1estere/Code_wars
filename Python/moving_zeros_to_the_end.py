def move_zeros(array):
    zeros_count = array.count(0)

    for el in array:
        for i in range(zeros_count):
            if (el == 0):
                array.remove(el)

    for i in range(zeros_count):
        array.append(0)

    return array