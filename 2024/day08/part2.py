
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

from collections import defaultdict
ants = defaultdict(list)
for i in range(m):
    for j in range(n):
        if lines[i][j] != '.':
            ants[lines[i][j]].append((i, j))

antigrid = [[False for _ in range(n)] for _ in range(m)]
for ant in ants:
    coords = ants[ant]
    for first in range(len(coords)):
        for second in range(len(coords)):
            if first == second: continue
            di = coords[second][0] - coords[first][0]
            dj = coords[second][1] - coords[first][1]
            i, j = coords[first][0], coords[first][1]
            while in_range(i, j):
                antigrid[i][j] = True
                i += di
                j += dj

ans = sum(sum(row) for row in antigrid)
print(ans)
