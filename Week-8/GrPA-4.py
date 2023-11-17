def steps(n):
    if n == 0:
        return 1
    if n == 1 or n == 2:
        return n
    s = 0
    s += steps(n-1)
    s += steps(n-2)
    s += steps(n-3)
    return s


# print(steps(5))
