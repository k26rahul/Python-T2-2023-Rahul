def factors(n):
    return set(
        i for i in range(1, n + 1) if n % i == 0
    )


def common_factors(a, b):
    return set(factors(a)) & set(factors(b))


def factors_upto(n):
    D = {}
    for i in range(1, n + 1):
        D[i] = factors(i)
    return D


print(factors(10))
print(common_factors(10, 5))
print(factors_upto(4))
