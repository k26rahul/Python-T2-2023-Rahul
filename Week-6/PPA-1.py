sequence = input().split(',')
freq = {
    word: sequence.count(word) for word in set(sequence)
}
