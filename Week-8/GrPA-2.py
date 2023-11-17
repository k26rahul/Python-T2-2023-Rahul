def linear(P, Q, k):
    if len(P) != len(Q):
        return False
    if len(P) == 0:
        return True
    if P[0] != k*Q[0]:
        return False
    return linear(P[1:], Q[1:], k)
