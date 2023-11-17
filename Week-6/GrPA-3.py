def rotate(mat):
    return [
        list(reversed(
            [row[i] for row in mat]
        )) for i in range(len(mat[0]))
    ]
