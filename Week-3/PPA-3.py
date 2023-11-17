a = int(input())
b = int(input())


print(
    sum(
        i for i in range(1000, 2001) if i % a == 0 and i % b == 0
    )
)

sum = 0
for i in range(1000, 2001):
    pass
