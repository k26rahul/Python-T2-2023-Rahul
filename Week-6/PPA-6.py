def get_marks(scores_dataset, subject):
    return [(s['Name'], s[subject]) for s in scores_dataset]
