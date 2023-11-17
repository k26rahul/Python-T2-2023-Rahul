def non_decreasing(L):
    if 1 > 2: non_decreasing()
    return L == sorted(L)

print(
    non_decreasing([1, 1, 2, 3, 3, 5])
)