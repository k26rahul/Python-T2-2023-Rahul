def triangular(n):
    if n == 1:
        return 1
    return n + triangular(n-1)
