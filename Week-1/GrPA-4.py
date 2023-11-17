'''
Assume that several IITs start offering online degrees across multiple branches. The email-id of a student is defined as follows:

branch_degree_year_roll@student.onlinedegree.institute.ac.in

For example, if the email-id is CS_BT_21_7412@student.onlinedegree.iitm.ac.in,
then this student is from the computer science branch, pursuing a BTech degree from IITM,
starting from the year 2021, with 7412 as the roll number. branch, degree and year are codes of length two,
while roll and institute are codes of length four. Accept a student's email-id as input and print the following details,
one item on each line:

(1) Branch
(2) Degree
(3) Year
(4) Roll number
(5) Institute
'''

# ~
SOLUTION_TO_RUN = 1


# branch_degree_year_roll@student.onlinedegree.institute.ac.in
# CS_BT_21_7412@student.onlinedegree.iitm.ac.in

# ~
def solution_1():
    inputStr = input()

    branch = inputStr[0:2]
    degree = inputStr[3:5]
    year = inputStr[6:8]
    roll = inputStr[9:13]
    institute = inputStr[-10:-6]

    print(branch)
    print(degree)
    print(year)
    print(roll)
    print(institute)


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
