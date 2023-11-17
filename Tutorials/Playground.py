def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[n]


print(fibonacci_iterative(10))


def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


print(fibonacci_recursive(10))

# > fib(10)
# = [fib(9) + fib(8)]
# = [34 + 21]
# = 55

# > fib(10)
# = [fib(9) + fib(8)]
# = [fib(8) + fib(7)] + [fib(7) + fib(6)]
# = [21 + 13] + [13 + 5]
# = [34 + 21]
# = 55

# ... And you will keep going and going further down the recursion tree, until you reach the base case: fib(1) or fib(0)
# Note: fib is short for fibonacci_recursive

# > sum_of_digits(1695)
# = 5 + sum_of_digits(196)
# = 5 + 16
# = 21

# > sum_of_digits(169)
# = 9 + sum_of_digits(16)
# = 9 + 7
# = 16

# > sum_of_digits(16)
# = 6 + sum_of_digits(1)
# = 6 + 1
# = 7

# > sum_of_digits(1)
# = 1
