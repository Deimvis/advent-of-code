
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
grid = [[lines[i][j] for j in range(n)] for i in range(m)]

in_range = lambda x,y: 0 <= x < m and 0 <= y < n
from itertools import product
dirs = list(product([-1, 0, 1], [-1, 0, 1]))

target = 'XMAS'
def is_word(i, j, d):
    for step in range(4):
        if not in_range(i, j): return False
        if grid[i][j] != target[step]: return False
        i = i + d[0]
        j = j + d[1]
    return True


ans = 0
for i in range(m):
    for j in range(n):
        for d in dirs:
            ans += is_word(i, j, d)
print(ans)
