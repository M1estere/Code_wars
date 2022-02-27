def square_digits(num):
    num = abs(num)
    result = ''

    while (num > 0):
        result = str((num % 10) ** 2) + result
        num //= 10
    return int(result) if result else 0


print(square_digits(int(input())))