def calc_radius(length):
    neg = False
    sum = 0

    for l in length[::-1]:
        if not neg:
            sum += l
        else:
            sum -= l
        neg = not neg

    if neg:
        return sum * 2, 3
    else:
        return -sum * 2, 1


def check(r, scale, length):
    next_r = length - r
    if r < scale or next_r < scale:
        return None
    return next_r


def solution(pegs):
    if len(pegs) < 2:
        return [-1, -1]

    pegs.sort()

    length = [pegs[i] - pegs[i - 1] for i in range(1, len(pegs))]

    r, scale = calc_radius(length)

    if scale != 1:
        length = [l * scale for l in length]

    if r < scale * 2:
        return [-1, -1]

    i = 0
    next_r = r
    while next_r is not None and i < len(length) - 1:
        next_r = check(next_r, scale, length[i])
        i += 1

    if next_r is None:
        return [-1, -1]
    if r % scale == 0:
        r /= scale
        scale = 1
    return [r, scale]
