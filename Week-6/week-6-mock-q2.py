sequence = input().split(',')
real_dict = {}

for word in sequence:
    if word[0] not in real_dict:
        real_dict[word[0]] = []

    real_dict[word[0]].append(word)
