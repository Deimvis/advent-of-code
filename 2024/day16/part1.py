
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
h = [(0, starti, startj, (0, 1))]
heapq.heapify(h)
seen = set([(starti, startj, (0, 1))])
while h:
    score, i, j, d = heapq.heappop(h)
    di, dj = d
    
    if grid[i][j] == 'E':
        print(score)
        import sys
        sys.exit()
    
    i1, j1 = i+di, j+dj
    if in_range(i1, j1) and grid[i1][j1] != '#' and (i1, j1, d) not in seen:
        seen.add((i1, j1, d))
        heapq.heappush(h, (score+1, i1, j1, d))
    for d1 in rotations[d]:
        if (i, j, d1) not in seen:
            seen.add((i, j, d1))
            heapq.heappush(h, (score+1000, i, j, d1))


