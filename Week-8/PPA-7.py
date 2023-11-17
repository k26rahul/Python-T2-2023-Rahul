def count(L, word):
    if len(L) == 0:
        return 0
    return int(L[0] == word) + count(L[1:], word)
