
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

grid = lines
seen = [[False for _ in range(n)] for _ in range(m)]
def bfs(i, j):
    area = 1
    per = 0
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        i1, j1 = i+di,j+dj
        if not in_range(i1, j1):
            per += 1
            continue
        if grid[i][j] != grid[i1][j1]:
            per += 1
            continue
        if seen[i1][j1]: continue
        seen[i1][j1] = True
        area1, per1 = bfs(i1, j1)
        area += area1
        per += per1
    return area, per


ans = 0
for i in range(m):
    for j in  range(n):
        if not seen[i][j]:
            seen[i][j] = True
            area, per = bfs(i, j)
            ans += area*per
print(ans)
