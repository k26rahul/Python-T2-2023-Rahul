import os
os.chdir('C:\k26rahul\Code\IITM-BS-Python\Week-9')


def add_period(filename):
    i = open(filename, "r")
    o = open('out.txt', "w")

    o.write('\n'.join(line.rstrip() + '.' for line in i))

    i.close()
    o.close()


add_period('public_1.txt')
