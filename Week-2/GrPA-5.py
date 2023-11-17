password = input()

if 8 <= len(password) <= 32 and password[0].isalpha() and \
        '/' not in password and '\\' not in password and '=' not in password and '"' not in password and \
        "'" not in password and ' ' not in password:
    print('True')
else:
    print('False')