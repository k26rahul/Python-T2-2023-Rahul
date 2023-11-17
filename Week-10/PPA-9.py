import os
os.chdir('C:\k26rahul\Code\IITM-BS-Python\Week-9')


def extract_lines(filename):
    csv = [row.split(',') for row in open(filename, 'r').read().split('\n')]

    csv = [row for row in csv[1:] if row[2] == 'M' and int(row[-2]) >= 70]

    o = 'SeqNo,Name,Gender,CT,Python,PDSA\n' + '\n'.join(
        ','.join(row) for row in csv
    )

    open('python.csv', 'w').write(o)


print(extract_lines('public_1.txt'))
