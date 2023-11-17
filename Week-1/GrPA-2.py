'''
Accept the date in DD-MM-YYYY format as input and print the year as output.
'''

# Sol 1
print(
    input()[-4:]
)


def other_solutions():
    # Sol 2
    print(
        input().split('-')[-1]
    )
