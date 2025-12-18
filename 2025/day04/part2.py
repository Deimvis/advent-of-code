
import sys
lines = [line.strip() for line in sys.stdin]

grid = lines
m = len(grid)
n = len(grid[0])

in_range = lambda x, y: 0 <= x < m and 0 <= y < n

cnts = [[-1 for _ in range(n)] for _ in range(m)]
from collections import deque
q = deque()
import itertools
for i in range(m):
    for j in range(n):
        if lines[i][j] == '@':
            cnt = 0
            for di, dj in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if di == dj == 0: continue
                i1 = i+di
                j1 = j+dj
                cnt += in_range(i1, j1) and lines[i1][j1] == '@'
            cnts[i][j] = cnt
            if cnt < 4:
                q.append((i, j))
                cnts[i][j] = -1

ans = 0
while len(q) > 0:
    i, j = q.popleft()
    ans += 1
    for di, dj in itertools.product([-1, 0, 1], [-1, 0, 1]):
        if di == dj == 0: continue
        i1, j1 = i+di, j+dj
        if in_range(i1, j1) and cnts[i1][j1] != -1:
            cnts[i1][j1] -= 1
            if cnts[i1][j1] < 4:
                q.append((i1, j1))
                cnts[i1][j1] = -1
print(ans)
