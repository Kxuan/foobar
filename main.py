alphas = [
    '100000',  # a
    '110000',  # b
    '100100',  # c
    '100110',  # d
    '100010',  # e
    '110100',  # f
    '110110',  # g
    '110010',  # h
    '010100',  # i
    '010110',  # j
    '101000',  # k
    '111000',  # l
    '101100',  # m
    '101110',  # n
    '101010',  # o
    '111100',  # p
    '111110',  # q
    '111010',  # r
    '011100',  # s
    '011110',  # t
    '101001',  # u
    '111001',  # v
    '010111',  # w
    '101101',  # x
    '101111',  # y
    '101011',  # z
]
capital = '000001'
space = '000000'


def trans(c):
    asc = ord(c)
    if asc >= ord('A') and asc <= ord('Z'):
        return capital + alphas[asc - ord('A')]
    elif asc >= ord('a') and asc <= ord('z'):
        return alphas[asc - ord('a')]
    elif asc == ord(' '):
        return space


def solution(s):
    return ''.join([trans(c) for c in s])
