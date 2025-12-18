
EMPTY_LINE_SIZE = 10**6

with open('input.txt') as f:
    matrix = [list(line) for line in f.read().strip().split('\n')]

m, n = len(matrix), len(matrix[0])
empty_rows = set()
for row in range(m):
    if all(map(lambda c: c == '.', matrix[row])):
        empty_rows.add(row)
empty_cols = set()
for col in range(n):
    column = [matrix[i][col] for i in range(m)]
    if all(map(lambda c: c == '.', column)):
        empty_cols.add(col)

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
                step_size = 1
                if i in empty_rows and di != 0:
                    step_size = EMPTY_LINE_SIZE
                if j in empty_cols and dj != 0:
                    step_size = EMPTY_LINE_SIZE
                q.append((i1, j1, dist+step_size))
ans //= 2
print(ans)
