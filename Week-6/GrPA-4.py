def two_level_sort(scores):
    scores = scores[:]
    scores.sort(key=lambda t: t[0])
    scores.sort(key=lambda t: t[1])
    return scores


print(two_level_sort(
    [('Sachin', 70), ('Sam', 69), ('Anirudh', 70), ('Anita', 80)]
))
