n = int(input())

input()

mat1 = [[
   int(x) for x in input().split()
] for i in range(n)]

input()

mat2 = [[
   int(x) for x in input().split()
] for i in range(n)]

# print(mat1)
# print(mat2)

sum_mat = [
    ['0' for j in range(n)] for i in range(n)
]

for i in range(n):
    for j in range(n):
        if i == j or j == n - 1 - i:
            sum_mat[i][j] = str(mat1[i][j] + mat2[i][j])

# print(sum_mat)

for row in sum_mat:
    print(' '.join(row))