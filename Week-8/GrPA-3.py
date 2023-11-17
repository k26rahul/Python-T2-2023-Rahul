def collatz(n):
    if n == 1:
        return 0
    c = n/2 if n % 2 == 0 else 3*n+1
    return 1 + collatz(c)
