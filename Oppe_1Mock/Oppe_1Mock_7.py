def mentors(scores_dataset, subject):
    dictionary = {}
    for X in scores_dataset:
        dictionary[X['SeqNo']] = [Y['SeqNo']
                                  for Y in scores_dataset if 10 <= X[subject] - Y[subject] <= 20]

    return dictionary
