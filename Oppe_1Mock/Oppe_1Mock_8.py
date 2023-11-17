def exactly_two(players):
    return set(player for player in players.keys() if sum(
        players[player].values()
    ) == 2)
