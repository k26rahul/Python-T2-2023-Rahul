def write_AP(a_1, d, n):
    sequence = [str(a_1 + x * d) for x in range(n)]
    f = open("out.txt", "w")
    f.write('\n'.join(sequence))
    f.close()
