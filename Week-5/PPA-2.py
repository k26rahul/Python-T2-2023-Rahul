def check_leap_year(y):
    if y % 100 == 0:
        return True if y % 400 == 0 else False
    else:
        return True if y % 4 == 0 else False
