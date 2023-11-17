def factors(n):
    return set(
        x for x in range(1, n + 1) if n % x == 0
    )


def common_factors(a, b):
    return factors(a) & factors(b)


def factors_upto(n):
    return {
        x: factors(x) for x in range(1, n + 1)
    }
