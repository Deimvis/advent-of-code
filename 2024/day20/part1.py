
grid = []
with open('input.txt') as f:
    grid = [[c for c in line.strip()] for line in f]

m, n = len(grid), len(grid[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

THRESHOLD = 100

starti = startj = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'S':
            starti,startj = i,j


path = [(starti, startj)]
i, j = starti, startj
previ, prevj = None, None
while grid[i][j] != 'E':
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for di, dj in dirs:
        i1 = i + di
        j1 = j + dj
        if in_range(i1, j1) and grid[i1][j1] != '#' and (i1, j1) != (previ, prevj):
            previ,prevj = i,j
            i,j = i1,j1
            path.append((i, j))
            break

p2dist = {}
for i in range(len(path)):
    p2dist[path[i]] = len(path)-1-i 


ans = 0
for (i, j) in path:
    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for di, dj in dirs:
        i1 = i + 2*di
        j1 = j + 2*dj 
        if in_range(i1, j1) and grid[i1][j1] != '#':
            if p2dist[(i, j)] - (p2dist[(i1, j1)] + 2) >= THRESHOLD:
                ans += 1
print(ans)
