def matrix_type(M):
    n = len(M)

    isDiagonal, isScalar, isIdentity = True, True, True
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] != 0:
                isDiagonal = False
            if i == j and M[i][j] != M[0][0]:
                isScalar = False
            if i == j and M[i][j] != 1:
                isIdentity = False

    if not isDiagonal:
        return 'non-diagonal'

    if isIdentity:
        return 'identity'

    return 'scalar' if isScalar else 'diagonal'
