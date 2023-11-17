def get_toppers(scores_dataset, subject, gender):
    scores_dataset = sorted(
        [
            (s['Name'], s[subject]) for s in scores_dataset if s['Gender'] == gender
        ],
        key=lambda s: s[1], reverse=True
    )

    return [s[0] for s in scores_dataset if s[1] == scores_dataset[0][1]]
