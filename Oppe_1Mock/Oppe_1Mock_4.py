def exact_count(para, n):
    para = para.split(' ')

    # print([para.count(word) for word in para])

    return any([
        c == n for c in [
            para.count(word) for word in para
        ]
    ])


# print(exact_count(
#     'this is a sentence there are many sentences is working fine is good to go is',
#     5
# ))

print(exact_count(
    'good word many good works good real choice',
    3
))
