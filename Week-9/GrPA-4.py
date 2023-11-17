import os
os.chdir('C:\k26rahul\Code\IITM-BS-Python\Week-9')

number_words = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}


def num_to_words(mat):
    open('words.csv', 'w').write(
        '\n'.join(
            ','.join(
                [number_words[i] for i in row]
            ) for row in mat
        )
    )


num_to_words(
    [[9, 7, 2], [1, 0, 5], [5, 2, 6]]
)
