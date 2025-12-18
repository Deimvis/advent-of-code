
grid = []
with open('input.txt') as f:
    grid = [[c for c in line.strip()] for line in f]

m, n = len(grid), len(grid[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n


for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            starti, startj = i, j

rotations = {
    (0, 1): [(-1, 0), (1, 0)],
    (1, 0): [(0, -1), (0, 1)],
    (0, -1): [(-1, 0), (1, 0)],
    (-1, 0): [(0, -1), (0, 1)],
}
import heapq
h = [(0, starti, startj, (0, 1), [(starti, startj, (0, 1))])]
heapq.heapify(h)
from collections import defaultdict
seen = defaultdict(lambda: float('+inf'))
seen[(starti, startj, (0, 1))] = 0
best_score = None
best_seats = set()
while h:
    score, i, j, d, path = heapq.heappop(h)
    di, dj = d

    if best_score is not None and score > best_score:
        break
    
    if grid[i][j] == 'E':
        best_score = score
        for i, j, _ in path:
            best_seats.add((i, j))

    i1, j1 = i+di, j+dj
    if in_range(i1, j1) and grid[i1][j1] != '#' and score+1 <= seen[(i1, j1, d)]:
        seen[(i1, j1, d)] = score+1
        path1 = path[:]
        path1.append((i1, j1, d))
        heapq.heappush(h, (score+1, i1, j1, d, path1))
    for d1 in rotations[d]:
        if score+1000 <= seen[(i, j, d1)]:
            seen[(i, j, d1)] = score+1000
            path1 = path[:]
            path1.append((i, j, d1))
            heapq.heappush(h, (score+1000, i, j, d1, path1))

print(len(best_seats))
