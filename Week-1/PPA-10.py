'''
The police are trying to track a criminal based on the evidence available at a crime site.
Their main clue is a vehicle's damaged number plate. Only the string TN07 is visible.
The format of the registration number is AA00AA00, where the first two letters are alphabets, next two are numbers,
    next two are again alphabets followed by two numbers at the end. A number plate is picked from a database of registration numbers
    and is given to you as input. Your task is to determine if this could belong to the criminal or not.
Print True if the number plate contains TN07 and False otherwise.
'''

numberPlate = input()
print(numberPlate[0:4] == 'TN07' or numberPlate[4:] == 'TN07')
