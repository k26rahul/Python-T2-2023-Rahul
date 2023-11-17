def add_period(filename):
    i = open(filename, "r")
    o = open('out.txt', "w")

    o.write('\n'.join(line.rstrip() + '.' for line in i))

    i.close()
    o.close()
