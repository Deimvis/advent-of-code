
grid = []
movements = []
with open('input.txt') as f:
    grid_raw, movements_raw = f.read().split('\n\n')
    for line in grid_raw.split():
        row = [c for c in line.strip()]
        grid.append(row)
    for line in movements_raw:
        movements.extend([c for c in line.strip()])


m, n = len(grid), len(grid[0])
in_range = lambda x, y: 0 <= x < m and 0 <= y < n


starti = startj = None
for i in range(m):
    for j in range(n):
        if grid[i][j] == '@':
            starti = i
            startj = j
            break

i,j = starti,startj
for move in movements:
    d = None
    if move == '^':
        d = (-1, 0)
    elif move == '>':
        d = (0, 1)
    elif move == 'v':
        d = (1, 0)
    else:
        d = (0, -1)

    i1,j1 = i+d[0],j+d[1]
    di,dj=d
    if grid[i1][j1] == '#':
        continue
    if grid[i1][j1] == 'O':
        i2,j2=i1,j1
        while grid[i2][j2] == 'O':
            i2,j2=i2+di,j2+dj
        if grid[i2][j2] == '#':
            continue
    
        grid[i2][j2] = grid[i1][j1]
    
        grid[i1][j1] = '@'
        grid[i][j] = '.'
        i,j=i1,j1
    else:
        grid[i1][j1] = '@'
        grid[i][j] = '.'
        i,j=i1,j1

ans = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'O':
            ans += 100*i+j
print(ans)

