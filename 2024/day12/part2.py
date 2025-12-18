
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

grid = lines
seen = [[False for _ in range(n)] for _ in range(m)]
def bfs(i, j):
    area = 1
    angles = 0
    # diags
    import itertools
    for di, dj in itertools.product([-1,1],[-1,1]):
        i1,j1=i+di,j+dj
        neigh1 = in_range(i1,j) and grid[i][j] == grid[i1][j]
        neigh2 = in_range(i,j1) and grid[i][j] == grid[i][j1]
        if not neigh1 and not neigh2:
            angles += 1
            continue
        if not in_range(i1,j1) or grid[i][j] != grid[i1][j1]:
            if neigh1 and neigh2:
                angles += 1
                continue
            elif neigh1:
                continue
            elif neigh2:
                continue
            else:
                raise RuntimeError('no neighs')
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        i1, j1 = i+di,j+dj
        if not in_range(i1, j1):
            continue
        if grid[i][j] != grid[i1][j1]:
            continue
        if seen[i1][j1]: continue
        seen[i1][j1] = True
        area1, angles1 = bfs(i1, j1)
        area += area1
        angles += angles1
    return area, angles


ans = 0
for i in range(m):
    for j in  range(n):
        if not seen[i][j]:
            seen[i][j] = True
            area, angles = bfs(i, j)
            ans += area*angles
print(ans)
