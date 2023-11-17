def non_decreasing(L):
    if len(L) == 1:
        return True
    if L[0] > L[1]:
        return False
    return non_decreasing(L[1:])
