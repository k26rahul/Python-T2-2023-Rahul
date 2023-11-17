'''
Accept two positive integers M and N as input. There are two cases to consider:

(1) If M < N, then print M as output.

(2) If M >= N, subtract N from M. Call the difference M1. If M1 >= N,
    then subtract N from M1 and call the difference M2.
    Keep doing this operation until you reach a value k, such that, Mk < N.
    You have to print the value of Mk as output.
    You should be able to solve this problem using the concepts covered in week-1.
'''

# ~
SOLUTION_TO_RUN = 1


# ~
def solution_1():
    m = int(input())
    n = int(input())

    while (m >= n):
        m -= n

    print(m)


def solution_2():
    pass


def solution_3():
    pass


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
