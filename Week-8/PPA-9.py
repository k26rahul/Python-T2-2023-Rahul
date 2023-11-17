def uniq(L):
    if len(L) == 0:
        return []

    if L[0] in L[1:]:
        return uniq(L[1:])

    return [L[0], *uniq(L[1:])]
