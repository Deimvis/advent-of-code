
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n


starti = -1
startj = -1
for i in range(m):
    for j in range(n):
        if lines[i][j] == '^':
            starti, startj = i, j
            break

def solve(grid):
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dind = 0
    d = dirs[dind]
    i, j = starti, startj
    seen = [[False for _ in range(n)] for _ in range(m)]
    in_loop = False
    while True:
        if in_range(i+d[0], j+d[1]) and grid[i+d[0]][j+d[1]] == '#' and seen[i][j]:
            in_loop = True
            break
        while in_range(i+d[0], j+d[1]) and grid[i+d[0]][j+d[1]] == '#':
            seen[i][j] = True
            dind = (dind+1)%len(dirs)
            d = dirs[dind]
        if not in_range(i+d[0], j+d[1]): break
        i += d[0]
        j += d[1]
    return in_loop

lines = [[lines[i][j] for j in range(n)] for i in range(m)]


ans = 0
for i in range(m):
    for j in range(n):
        if lines[i][j] == '.':
            newgrid = [line[::] for line in lines]
            newgrid[i][j] = '#'
            ans += solve(newgrid)
print(ans)
