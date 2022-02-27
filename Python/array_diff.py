def array_diff(a, b):
    for el in b:
        if (el in a):
            for i in range(a.count(el)):
                a.remove(el)

    return a