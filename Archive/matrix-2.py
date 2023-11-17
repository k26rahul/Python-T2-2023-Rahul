matrix = [
    [8, 5, 2, 3, 1],
    [4, 6, 9, 2, 7],
    [3, 9, 8, 5, 1],
    [7, 1, 1, 4, 9],
    [2, 6, 3, 7, 1],
]

# Programmatically get the submatrix without the row=2 and column=2
# matrix = [
#     [8, 2, 3, 1],
#     [3, 8, 5, 1],
#     [7, 1, 4, 9],
#     [2, 3, 7, 1],
# ]

i, j = 1, 1  # Zero based indexing

# print(matrix[:i])
# > [[8, 5, 2, 3, 1]]

# print(matrix[i+1:])
# > [[3, 9, 8, 5, 1], [7, 1, 1, 4, 9], [2, 6, 3, 7, 1]]

# print(matrix[:i] + matrix[i+1:])
# > [[8, 5, 2, 3, 1], [3, 9, 8, 5, 1], [7, 1, 1, 4, 9], [2, 6, 3, 7, 1]]

for row in matrix[:i] + matrix[i+1:]:
    print(row)
# Received output:
# > [8, 5, 2, 3, 1]
# > [3, 9, 8, 5, 1]
# > [7, 1, 1, 4, 9]
# > [2, 6, 3, 7, 1]
# It is clearly visible that row=2 -> [4, 6, 9, 2, 7] is missing, and it's precisely what we are trying to do

for row in matrix[:i] + matrix[i+1:]:
    print(row[:j], row[j+1:])
# Received output:
# > [8] [2, 3, 1]
# > [3] [8, 5, 1]
# > [7] [1, 4, 9]
# > [2] [3, 7, 1]
# It is similar to the last output, except the fact that second column is missing.
# Next, what we're going to do is to join them both ✌️

for row in matrix[:i] + matrix[i+1:]:
    print(row[:j] + row[j+1:])
# Received output:
# > [8, 2, 3, 1]
# > [3, 8, 5, 1]
# > [7, 1, 4, 9]
# > [2, 3, 7, 1]
# We successfully completed our objective ✅

print([
    row[:j] + row[j+1:] for row in matrix[:i] + matrix[i+1:]
])
# > [[8, 2, 3, 1], [3, 8, 5, 1], [7, 1, 4, 9], [2, 3, 7, 1]]
# The same for loop written in a concise syntax
