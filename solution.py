def minus(x, y, base):
    r = [0] * len(x)

    for i in range(len(x)):
        r[i] = x[i] - y[i]
        j = i
        while j > 0 and r[j] < 0:
            r[j] += base
            j -= 1
            r[j] -= 1
    return tuple(r)


def solution(n, b):
    n = [int(dgt) for dgt in n]
    result = {tuple(n): 0}

    i = 1
    while True:
        y = sorted(n)
        x = y[::-1]
        z = minus(x, y, b)
        if z in result:
            return i - result[z]
        result[z] = i
        n = z
        i += 1
