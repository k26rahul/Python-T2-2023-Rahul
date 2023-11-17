def get_freq(filename):
    words = open(filename, 'r').read().split('\n')
    return {key: words.count(key) for key in set(words)}
