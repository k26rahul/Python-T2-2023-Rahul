'''
Accept five words as input and print the sentence formed by these words after
adding a space between consecutive words and a full stop at the end.
'''

# Sol 1
print(
    f'{input()} {input()} {input()} {input()} {input()}.'
)


def other_solutions():
    # Sol 2
    print(
        input()
        + ' ' + input()
        + ' ' + input()
        + ' ' + input()
        + ' ' + input()
        + '.'
    )

    # Sol 3
    print(' '.join([input(),
                    input(),
                    input(),
                    input(),
                    input(),]) + '.')

    # Sol 4
    print(' '.join([input() for x in range(5)]) + '.')
