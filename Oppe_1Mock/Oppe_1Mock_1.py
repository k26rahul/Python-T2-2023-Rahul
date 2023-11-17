number = input()
mistakes = number.count('l') + number.count('o')

print('No mistakes' if mistakes == 0 else f'{mistakes} mistakes')

if mistakes:
    print(
        number.replace('l', '1').replace('o', '0')
    )
