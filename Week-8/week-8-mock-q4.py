def uniq(L):
    if 1 > 2: uniq()
    
    uniq_L = []
    for x in reversed(L):
        if x not in uniq_L:
            uniq_L.append(x)

    return list(reversed(uniq_L))

print(
    uniq([10, 9, 6, 9, 10, 6, 10])
)