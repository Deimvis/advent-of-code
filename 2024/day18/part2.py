
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]


m = n = 70 + 1 
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

import re
fallen_bytes = [(i, j) for j, i in map(lambda line: map(int, re.findall(r'\d+', line)), lines)]

def has_solution(bytes_cnt) -> bool:
    grid = [['.' for _ in range(n)] for _ in range(m)]
    for i, j in fallen_bytes[:bytes_cnt]:
        grid[i][j] = '#'

    from collections import deque
    q = deque([(0, 0)])
    seen = set()
    steps = 0
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i == m-1 and j == n-1:
                return True
            dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            for di, dj in dirs:
                i1 = i + di
                j1 = j + dj
                if in_range(i1, j1) and grid[i1][j1] == '.' and (i1, j1) not in seen:
                    seen.add((i1, j1))
                    q.append((i1, j1))
        steps += 1
    return False

l = 0
r = len(fallen_bytes)-1
while l < r:
    m = l + (r - l) // 2
    if has_solution(m):
        l = m + 1
    else:
        r = m

i, j = fallen_bytes[l-1]
print(f'{j},{i}')
