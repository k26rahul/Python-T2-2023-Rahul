n = int(input())
matrix = [input().split(' ') for _ in range(n)]

print(matrix[1])
print([row[1] for row in matrix])

d1 = []
for i in range(n):
    d1.append(matrix[i][i])
print(d1)

d2 = []
for i in range(n):
    d2.append(matrix[i][n - 1 - i])
print(d2)

# matrix = []
# for i in range(n):
#     matrix.append(
#         input().split(' ')
#     )

# row_0 = input().split(' ')
# row_1 = input().split(' ')
# row_2 = input().split(' ')
# row_3 = input().split(' ')
# row_4 = input().split(' ')

# matrix = [row_0,
#           row_1,
#           row_2,
#           row_3,
#           row_4,]

# print(matrix[1])
# print(type(matrix))
# print(type(matrix[0]))

# j = 4
# print([
#     matrix[0][j],
#     matrix[1][j],
#     matrix[2][j],
#     matrix[3][j],
#     matrix[4][j],
# ])

# j = 0
# col = []
# for i in range(n):
#     col.append(
#         matrix[i][j]
#     )
# print(col)

# col = [matrix[i][0] for i in range(n)]
# print(col)

# j = 0
# col = []
# for row in matrix:
#     col.append(
#         row[j]
#     )
# print(col)

# col = [row[0] for row in matrix]
# print(col)
