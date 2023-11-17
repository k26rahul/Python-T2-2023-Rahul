n = int(input())
station_dict = {}
for i in range(n):
    train = input()
    station_dict[train] = {}
    m = int(input())
    for i in range(m):
        compartment, passengers = input().split(',')
        station_dict[train][compartment] = int(passengers)

print(station_dict)
