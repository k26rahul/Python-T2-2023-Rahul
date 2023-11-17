string = input()

if '.' in string and string.replace('-', '').replace('.', '').isdigit():
    print('Float')
else:
    print('Integer' if string.replace('-', '').isdigit() else 'None')
