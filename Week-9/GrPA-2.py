def relation(file1, file2):
    file1 = open(file1, 'r').read().split('\n')
    file2 = open(file2, 'r').read().split('\n')
    if file1 == file2:
        return 'Equal'
    return 'Subset' if file2[:len(file1)] == file1 else 'No Relation'
