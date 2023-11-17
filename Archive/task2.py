k = [int(x) for x in input().split(',')]

sorted_k = []

while k:
    max = 0
    for x in k:
        if x > max:
            max = x
    sorted_k.append(max)
    k.remove(max)

# print(min)
print(sorted_k)

# max = 0
# for x in k:
#     if x > max:
#         max = x

# print(max)

# print(min(k))
# print(max(k))

# 12,7,5,100,36,2