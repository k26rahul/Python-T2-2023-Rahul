def is_empty(L):
    return len(L) == 0


def first(L):
    return L[0] if len(L) > 0 else 'None'


def last(L):
    return L[-1] if len(L) > 0 else 'None'


def init(L):
    return L[:-1] if len(L) > 0 else 'None'


def rest(L):
    return L[1:] if len(L) > 0 else 'None'
