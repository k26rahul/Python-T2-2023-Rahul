# print([
#     int(x) for x in input().split(',')
# ])

sequence = [int(x) for x in input().split(',')]
left = sum(sequence[:len(sequence)//2])
right = sum(sequence[len(sequence)//2:])

# left = sequence[:len(sequence)//2]
# print(left, sum(left))

# right = sequence[len(sequence)//2:]
# print(right, sum(right))

if left == right:
    print('balanced')
else:
    # if left > right:
    #     print()
    # else:
    #     print()
    print('left-heavy' if left > right else 'right-heavy')
