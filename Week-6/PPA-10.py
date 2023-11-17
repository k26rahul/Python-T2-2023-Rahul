def group_by_city(scores_dataset):
    cities = {}

    for entry in scores_dataset:
        if entry['City'] not in cities:
            cities[entry['City']] = []

        cities[entry['City']].append(entry['Name'])

    return cities


def busy_cities(scores_dataset):
    cities = sorted(
        [
            (key, value) for key, value in group_by_city(scores_dataset).items()
        ],
        key=lambda tup: len(tup[1]),
        reverse=True
    )
    return [key for key, value in cities if len(value) == len(cities[0][1])]
