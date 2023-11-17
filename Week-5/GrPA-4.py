def is_magic(mat):
    n = len(mat)

    rowSums = [sum(row) for row in mat]

    columnSums = [sum(
        row[i] for row in mat
    ) for i in range(n)]

    diagonalSums = [
        sum(mat[i][i] for i in range(n)),
        sum(mat[i][n - 1 - i] for i in range(n))
    ]

    return 'YES' if all(val == rowSums[0] for val in [
        *rowSums, *columnSums, *diagonalSums
    ]) else 'NO'
