def descending_order(num):
    digits_array = [int(d) for d in str(num)]

    digits_array.sort(reverse=True)

    result = ""

    for number in range(len(digits_array)):
        result += str(digits_array[number])

    return int(result)