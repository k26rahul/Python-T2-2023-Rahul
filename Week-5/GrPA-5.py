def transpose(mat):
    return [
        [row[i] for row in mat]
        for i in range(len(mat[0]))
    ]


# print(transpose(
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ]
# ))
