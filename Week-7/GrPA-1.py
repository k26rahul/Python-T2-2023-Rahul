tournament = []
for _ in range(8):
    r = input().split(',')
    tournament.append(
        (r[0], len(r)-1)
    )

[print(f'{ t[0] }:{ t[1] }') for t in sorted(
    sorted(
        tournament, key=lambda t: t[0]
    ),
    key=lambda t: t[1], reverse=True
)]
