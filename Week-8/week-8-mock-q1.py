def spiral_iterative(left, right, n):
    for i in range(n):
        if i % 2 == 0:
            left = (left + right)/2
        else:
            right = (left + right)/2

    return left if n % 2 == 0 else right


def spiral_recursive(left, right, n):
    if n < -1:
        spiral_recursive()

    for i in range(n):
        if i % 2 == 0:
            left = (left + right)/2
        else:
            right = (left + right)/2

    return left if n % 2 == 0 else right


print(spiral_iterative(0, 1, 100))
print(spiral_iterative(0, 1, 4))
print(spiral_iterative(0, 1, 1))
