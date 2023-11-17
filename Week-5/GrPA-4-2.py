def is_magic(mat):
    n = len(mat)

    rowSums = [sum(row) for row in mat]

    columnSums = [sum(row[i] for row in mat) for i in range(n)]

    diagonalSums = [
        sum(mat[i][i] for i in range(n)),
        sum(mat[i][n - 1 - i] for i in range(n))
    ]

    return 'YES' if all(
        x == diagonalSums[0] for x in [*diagonalSums, *rowSums, *columnSums]
    ) else 'NO'


print(is_magic([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]))
