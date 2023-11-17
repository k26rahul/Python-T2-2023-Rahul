def freq_to_words(words):
    words = [(word, words.count(word)) for word in words]
    return {
        x: list(set(
            w[0] for w in words if w[1] == x
        ))
        for x in set(
            w[1] for w in words
        )
    }
