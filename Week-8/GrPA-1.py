def reverse(L):
    if len(L) == 0:
        return []
    return [L[-1], *reverse(L[:-1])]
