
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]


m = n = 70 + 1 
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

import re
grid = [['.' for _ in range(n)] for _ in range(m)]
for idx in range(1024):
    j, i = map(int, re.findall(r'\d+', lines[idx]))
    grid[i][j] = '#'


from collections import deque
q = deque([(0, 0)])
seen = set()
steps = 0
while q:
    for _ in range(len(q)):
        i, j = q.popleft()
        if i == m-1 and j == n-1:
            print(steps)
            import sys
            sys.exit()
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for di, dj in dirs:
            i1 = i + di
            j1 = j + dj
            if in_range(i1, j1) and grid[i1][j1] == '.' and (i1, j1) not in seen:
                seen.add((i1, j1))
                q.append((i1, j1))
    steps += 1
