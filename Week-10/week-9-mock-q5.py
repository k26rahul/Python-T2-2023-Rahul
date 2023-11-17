def number_grid(m, n):
    open('numgrid.csv', 'w').write(
        '\n'.join(
            ','.join(
                map(str, list(range(i * n + 1, n * (i + 1) + 1)
                              ))
            ) for i in range(m)
        )
    )


print(number_grid(5, 3))
