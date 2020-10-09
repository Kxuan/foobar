def solution(x, y):
    count = 0
    x = int(x)
    y = int(y)
    while x > 0 and y > 0:
        if x > y:
            count += x // y
            x %= y
        else:
            count += y // x
            y %= x

    if x < 0 or y < 0:
        return "impossible"
    elif (x == 0 and y == 1) or (x == 1 and y == 0):
        return str(count - 1)
    else:
        return "impossible"
