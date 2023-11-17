def get_matrix(filename):
    return [list(
        map(int, row.split(','))
    ) for row in open(filename, 'r').read().split()]
