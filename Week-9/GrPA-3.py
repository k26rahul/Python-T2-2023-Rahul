def get_goals(filename, country):
    data = [row.split(',')
            for row in open(filename, 'r').read().split()[1:]]

    num_players = 0
    num_goals = 0

    for row in data:
        if row[1] == country:
            num_players += 1
            num_goals += int(row[2])

    return (num_players, num_goals) if num_players > 0 else (-1, -1)
