'''
Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
'''

# ~
SOLUTION_TO_RUN = 2


# ~
def solution_1():
    inputStr = input()
    print(
        int(inputStr[0]) *
        int(inputStr[2]) *
        int(inputStr[4]) *
        int(inputStr[6]) *
        int(inputStr[8])
    )


def solution_2():
    # pass
    inputStr = input()
    product = 1
    for x in [int(x) for x in inputStr.split(',')]:
        product = product * x
    print(product)


def solution_3():
    # pass
    inputStr = input()
    num_1 = int(inputStr[0])
    num_2 = int(inputStr[2])
    num_3 = int(inputStr[4])
    num_4 = int(inputStr[6])
    num_5 = int(inputStr[8])
    print(
        num_1 * num_2 * num_3 * num_4 * num_5
    )


def solution_4():
    pass


# ~
if SOLUTION_TO_RUN == 1:
    solution_1()

elif SOLUTION_TO_RUN == 2:
    solution_2()

elif SOLUTION_TO_RUN == 3:
    solution_3()

elif SOLUTION_TO_RUN == 4:
    solution_4()
