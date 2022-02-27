import math


def is_square(n):
    if (n < 0): return False

    num_root = math.isqrt(n)

    if (num_root ** 2 == n):
        return True
    return False


print(is_square(int(input())))