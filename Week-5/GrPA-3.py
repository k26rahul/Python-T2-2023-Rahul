def distance(word1, word2):
    if len(word1) != len(word2):
        return -1
    return sum(
        [abs(ord(word1[i]) - ord(word2[i])) for i in range(len(word1))]
    )
