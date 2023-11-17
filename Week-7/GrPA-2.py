def merge(D1, D2, priority):
    if priority == 'first':
        return {**D2, **D1}
    else:
        return {**D1, **D2}


print(merge(
    {1: 2, 2: 3, 3: 4},
    {1: 10, 4: 15, 5: 10},
    'first',
))
