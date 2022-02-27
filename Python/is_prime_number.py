import math


def is_prime(num):
    if (num <= 0 or num == 1): return False

    counter = 0

    for i in range(1, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            counter += 1
        else:
            continue

    if (counter == 1): return True

    return False