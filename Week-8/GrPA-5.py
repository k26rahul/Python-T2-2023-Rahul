def ancestry(P, present, past):
    if present == past:
        return [past]
    return [present, *ancestry(P, P[present], past)]


print(ancestry(
    {'Jahangir': 'Akbar', 'Akbar': 'Humayun', 'Humayun': 'Babur'},
    'Jahangir',
    'Babur',
))
