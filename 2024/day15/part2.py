
grid = []
movements = []
with open('input.txt') as f:
    grid_raw, movements_raw = f.read().split('\n\n')
    for line in grid_raw.split():
        row = []
        for c in line:
            if c == '@':
                row.append(c)
                row.append('.')
            elif c == 'O':
                row.append('[')
                row.append(']')
            else:
                row.append(c)
                row.append(c)
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

def move(i, j, di, dj, perform):
    global grid
    if grid[i][j] == '.':
        return True
    if grid[i][j] == '#':
        return False
    if di == 0:
        if not move(i+2*di,j+2*dj,di,dj,False):
            return False
        if perform:
            assert move(i+2*di,j+2*dj,di,dj,True)
            grid[i+2*di][j+2*dj] = grid[i+di][j+dj]
            grid[i+di][j+dj] = grid[i][j]
            grid[i][j] = '.'
    else:
        i1,j1=i+di,j+dj
        if not move(i1,j1,di,dj,False):
            return False
        if grid[i][j] == '[':
            q,p = i,j+1
        else:
            q,p = i,j-1
        q1,p1=q+di,p+dj
        if not move(q1,p1,di,dj,False):
            return False
        if perform:
            assert move(i1,j1,di,dj,True)
            assert move(q1,p1,di,dj,True)
            grid[i1][j1] = grid[i][j]
            grid[q1][p1] = grid[q][p]
            grid[i][j] = '.'
            grid[q][p] = '.'
    return True

i,j = starti,startj
for direction in movements:
    d = None
    if direction == '^':
        d = (-1, 0)
    elif direction == '>':
        d = (0, 1)
    elif direction == 'v':
        d = (1, 0)
    else:
        d = (0, -1)

    i1,j1 = i+d[0],j+d[1]
    if move(i1,j1,d[0],d[1],True):
        grid[i1][j1] = '@'
        grid[i][j] = '.'
        i,j=i1,j1

ans = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == '[':
            ans += 100*i+j
print(ans)
