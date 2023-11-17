import os
os.chdir('C:\k26rahul\Code\IITM-BS-Python\Week-9')


def improvement(filename):
    f = open(filename, 'r')
    csv = [[
        int(x) for x in row.split(',')[2:]
    ] for row in f.read().split('\n')[1:]]

    return sum(1 if row[0] < row[1] < row[2] else 0 for row in csv)
