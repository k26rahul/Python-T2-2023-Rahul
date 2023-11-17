def crowded_group(scores_dataset, subject, mark_limit):
    scoreList = sorted(entry[subject] for entry in scores_dataset)
    groups = [0]
    minimumScoreInGroup = scoreList[0]
    for score in scoreList:
        if score - minimumScoreInGroup <= mark_limit:
            groups[-1] += 1
        else:
            groups.append(1)
            minimumScoreInGroup = score

    return max(groups)
