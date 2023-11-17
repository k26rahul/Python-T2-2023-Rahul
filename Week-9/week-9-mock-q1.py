import os
os.chdir('C:\k26rahul\Code\IITM-BS-Python\Week-9')


def write_AP(a_1, d, n):
    sequence = [str(a_1 + x * d) for x in range(n)]
    f = open("out.txt", "w")
    f.write('\n'.join(sequence))
    f.close()


write_AP(1, 3, 5)
