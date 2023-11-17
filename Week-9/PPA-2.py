def read_line(filename, n):
    s = open(filename, 'r').read().split('\n')
    return s[n-1] if n <= len(s) else None
