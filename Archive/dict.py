# phone_number = input()
# mistakes = 0
# if 'l' not in phone_number and 'o' not in phone_number:
#     print('No mistakes')
# else:
#     for digit in phone_number:
#         if digit == 'l' or digit == 'o':
#             mistakes += 1
#     phone_number = phone_number.replace('o', '0')
#     phone_number = phone_number.replace('l', '1')
#     print(str(mistakes) + ' mistakes')
#     print(phone_number)

dict = {
    'name': 'Sanika',
    'age': 20
}

# print(dict['name'])
# print(dict['age'])

# print(dict.keys())
# print(dict.values())
# print(dict.items())

# for key, val in dict.items():
#     print(key, val)

# tup = ('Sanika', 20)
# for x in tup:
#     print(x)

for x in dict.items():
    print(x)
