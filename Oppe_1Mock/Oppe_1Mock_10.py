def is_reachable(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'B':
                B = i, j
            if grid[i][j] == 'G':
                G = i, j

    isReachable = B[0] >= G[0]
    steps = None if not isReachable else abs(B[0] - G[0]) + abs(B[1] - G[1])
    return (isReachable, steps)


print(is_reachable([
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'G'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'B', 'W', 'W', 'W'],
]))
