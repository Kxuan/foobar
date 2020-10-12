def choose(n, k):
    s = 1
    for i in range(n, n - k, -1):
        s *= i
    for i in range(1, k + 1):
        s /= i
    return s


def solution(count, required):
    if required == 0:
        return [[]] * count

    column = choose(count, required - 1)
    map = [[i for i in range(column)] for j in range(count)]

    window = []
    for ci in range(required - 1):
        window.append(ci)

    for ci in range(column - 1, -1, -1):
        for ri in window:
            map[ri][ci] = None

        i = len(window) - 1
        while i >= 0:
            window[i] += 1
            if window[i] != count - len(window) + i + 1:
                break
            i -= 1
        end = i
        for i in range(end + 1, len(window)):
            window[i] = window[i - 1] + 1

    for ri in range(len(map)):
        map[ri] = [n for n in map[ri] if n is not None]
    return map
