def solution(n):
    n = int(n)
    op = 0
    while n > 3:
        s = n & 3
        if s == 0:  # div 2^2
            n = n >> 2
            op += 2
        elif s == 1:  # subtract 1 then div 2
            n = n >> 1
            op += 2
        elif s == 2:  # div 2
            n >>= 1
            op += 1
        else:  # add 1 then div 2^2
            n = (n + 1) >> 2
            op += 3

    if n == 0 or n == 2:
        op += 1
    elif n == 3:
        op += 2
    return op
