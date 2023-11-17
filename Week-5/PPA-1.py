def factorial(n):
    if n < 0:
        return -1

    p = 1
    while n:
        p *= n
        n -= 1

    return p


print(factorial(0))
