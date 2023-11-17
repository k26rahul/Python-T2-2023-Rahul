k = [input().split() for i in range(5)]

for i in range(5):
    k[i][1] = int(k[i][1])
    k[i][2] = int(k[i][2])

# k.sort(key=lambda el: el[1], reverse=True)
sorted_k = sorted(
    k, key=lambda el: el[1], reverse=True
)

[print(record[2]) for record in sorted_k]