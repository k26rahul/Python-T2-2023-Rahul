def search(L, k):
    if len(L) == 0:
        return False
    if L[0] == k:
        return True
    return search(L[1:], k)
