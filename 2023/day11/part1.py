
with open('input.txt') as f:
    matrix = [list(line) for line in f.read().strip().split('\n')]

m, n = len(matrix), len(matrix[0])
empty_rows = []
for row in range(m):
    if all(map(lambda c: c == '.', matrix[row])):
        empty_rows.append(row)
empty_cols = []
for col in range(n):
    column = [matrix[i][col] for i in range(m)]
    if all(map(lambda c: c == '.', column)):
        empty_cols.append(col)

shift = 0
for row in empty_rows:
    matrix.insert(row + shift, ['.']*n)
    shift += 1
m = m + shift
shift = 0
for col in empty_cols:
    for i in range(m):
        matrix[i].insert(col + shift, '.')
    shift += 1
n = n + shift

galaxies = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == '#':
            galaxies.append((i, j))

in_range = lambda x, y: 0 <= x < m and 0 <= y < n
ans = 0
for (start_i, start_j) in galaxies:
    seen = [[False for _ in range(n)] for _ in range(m)]
    seen[start_i][start_j] = True
    from collections import deque
    q = deque([(start_i, start_j, 0)])
    while q:
        i, j, dist = q.popleft()
        if matrix[i][j] == '#':
            ans += dist
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            i1 = i + di
            j1 = j + dj
            if in_range(i1, j1) and not seen[i1][j1]:
                seen[i1][j1] = True
                q.append((i1, j1, dist+1))
ans //= 2
print(ans)
