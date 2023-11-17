'''
Accept a positive integer x as input, compute the value of this continued fraction and store the result in a variable named cfrac.
We will round off your answer to exactly two decimal places. You don't have to print the output to the console, we will take care of that.
'''

x = int(input())
cfrac = x + 1/(
    x + 1/(
        x + 1/(
            x + 1/(
                x + 1/x
            )
        )
    )
)
