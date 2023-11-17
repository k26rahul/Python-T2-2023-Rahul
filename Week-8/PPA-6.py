def spiral_iterative(left, right, n):
    for i in range(n):
        left, right = right, (left + right)/2

        # if i % 2 == 0:
        #     left = (left + right)/2
        # else:
        #     right = (left + right)/2

    return left if n % 2 == 0 else right


def spiral_recursive(left, right, n):
    # print(f'{left=}, {right=}, {n=}')

    if n == 1:
        return right

    left, right = right, (left + right)/2

    # print(f'{left=}, {right=}, {n=}\n')
    return spiral_recursive(left, right, n - 1)


print(f'{spiral_iterative(0, 1, 4)=}')
print(f'{spiral_recursive(0, 1, 4)=}')
