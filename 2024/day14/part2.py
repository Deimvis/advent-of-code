

lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = 101, 103
# m, n = 7, 11
in_range = lambda x,y: 0 <= x < m and 0 <= y < n


xs = []
ys = []
dxs = []
dys = []
grid = [[False for _ in range(n)] for _ in range(m)]
for line in lines:
    import re
    match = re.match(r'p=([^ ]*) v=([^ ]*)', line)
    x0,y0 = map(int, match.group(1).split(','))
    dx,dy = map(int, match.group(2).split(','))
    xs.append(x0)
    ys.append(y0)
    dxs.append(dx)
    dys.append(dy)
    grid[x0][y0] = True

def make_step():
    global xs, ys, dxs, dys, grid
    grid = [[False for _ in range(n)] for _ in range(m)]
    for i in range(len(xs)):
        xs[i] = (xs[i] + dxs[i]) % m
        ys[i] = (ys[i] + dys[i]) % n
        grid[xs[i]][ys[i]] = True

ans = 0
for t in range(m*n):
    neighs = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
                for di, dj in dirs:
                    i1 = i + di
                    j1 = j + dj
                    if not in_range(i1, j1): continue
                    if grid[i1][j1]: neighs += 1
    if neighs > 500:
        ans = t
        break
    make_step()
print(ans)
