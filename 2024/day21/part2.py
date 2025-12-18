
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

panel1 = {
    '7': (0, 0),
    '8': (0, 1),
    '9': (0, 2),
    '4': (1, 0),
    '5': (1, 1),
    '6': (1, 2),
    '1': (2, 0),
    '2': (2, 1),
    '3': (2, 2),
    'forbidden': (3, 0),
    '0': (3, 1),
    'A': (3, 2),
}
panel2 = {
    'forbidden': (0, 0),
    '^': (0, 1),
    'A': (0, 2),
    '<': (1, 0),
    'v': (1, 1),
    '>': (1, 2),
}
def delta(src, dst):
    panel = panel1
    if src in panel2 and dst in panel2:
        panel = panel2
    i1, j1 = panel[src]
    i2, j2 = panel[dst]
    return i2-i1, j2-j1


DEPTH=26
from functools import cache


@cache
def is_valid(src, dst, di_first: bool):
    panel = panel1
    if src in panel2 and dst in panel2:
        panel = panel2
    badi, badj = panel['forbidden']
    i1, j1 = panel[src]
    i2, j2 = panel[dst]
    if not (min(i1,i2) <= badi <= max(i1,i2) and min(j1,j2) <= badj <= max(j1,j2)):
        return True
    if i1 == badi and not di_first:
        return False
    if j1 == badj and di_first:
        return False
    return True


@cache
def getpathlen(src, dst, left):
    if left == 0:
        return 2
    di, dj = delta(src, dst)
    dipart = ('^' if di < 0 else 'v')*abs(di)
    djpart = ('<' if dj < 0 else '>')*abs(dj)
    opt1 = dipart + djpart + 'A'
    opt2 = djpart + dipart + 'A'
    if not is_valid(src, dst, di_first=True):
        return transformlen(opt2, left-1)
    if not is_valid(src, dst, di_first=False):
        return transformlen(opt1, left-1)
    res1 = transformlen(opt1, left-1)
    res2 = transformlen(opt2, left-1)
    return res1 if res1 <= res2 else res2


def transformlen(s, left):
    if left == 0:
        return len(s)
    length = 0
    s = 'A' + s
    for i in range(len(s)-1):
        length += getpathlen(s[i], s[i+1], left)
    return length


import re
ans = 0
for line in lines:
    res_length = transformlen(line.strip(), DEPTH)
    num = int(re.search(r'\d+', line).group(0))
    ans += res_length * num
print(ans)
