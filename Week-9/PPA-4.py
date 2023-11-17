def get_dict(filename):
    data = [row.split(',')
            for row in open(filename, 'r').read().split('\n')[1:]]

    dictionary = {}
    for row in data:
        dictionary[row[0]] = int(row[1])

    return dictionary
