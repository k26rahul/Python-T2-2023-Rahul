def type_of_sequence(L):
    n = 0
    for w in L:
        n += int(mysterious(w))

    if n < 2:
        return 'mildly mysterious'
    else:
        return 'moderately mysterious' if n < 5 else 'most mysterious'
