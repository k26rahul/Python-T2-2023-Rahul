sequence = input().split(',')

real_dict = {
    key: [word for word in sequence if word[0] == key]
    for key in set(
        word[0] for word in sequence
    )
}
