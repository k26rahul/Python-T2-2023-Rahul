def get_range(L):
    return maxx(L) - minn(L)


def maxx(L):
    max = L[0]
    for i in L:
        if i > max:
            max = i
    return max


def minn(L):
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min
