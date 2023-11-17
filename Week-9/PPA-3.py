def get_max_line(filename):
    numbers = list(map(
        int, open(filename, 'r').read().split()
    ))
    return numbers.index(max(numbers)) + 1
