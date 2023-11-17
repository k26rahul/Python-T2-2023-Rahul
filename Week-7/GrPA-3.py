def minor_matrix(M, i, j):
    return [
        row[:j] + row[j+1:] for row in M[:i] + M[i+1:]
    ]


print(minor_matrix(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ],
    0,
    1,
))
