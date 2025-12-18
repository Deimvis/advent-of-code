

char2options = {
    '-': [(0, -1), (0, 1)],
    '|': [(-1, 0), (1, 0)],
    '7': [(0, -1), (1, 0)],
    'J': [(-1, 0), (0, -1)],
    'L': [(0, 1), (-1, 0)],
    'F': [(1, 0), (0, 1)],
}
def _go(char, i, j, prev_i, prev_j):
    for di, dj in char2options[char]:
        next_i = i + di
        next_j = j + dj
        if (next_i, next_j) == (prev_i, prev_j): continue
        return next_i, next_j

def _possible(char, i, j, to_i, to_j):
    for di, dj in char2options[char]:
        next_i = i + di
        next_j = j + dj
        if (next_i, next_j) == (to_i, to_j):
            return True
    return False


with open('input.txt') as f:
    matrix = [list(line) for line in f.read().strip().split('\n')]

m, n = len(matrix), len(matrix[0])
in_range = lambda x, y: 0 <= x < m and 0 <= y < n

def go(i, j, prev_i, prev_j):
    next_i, next_j = _go(matrix[i][j], i, j, prev_i, prev_j)
    if not in_range(next_i, next_j):
        return None, None, False
    if matrix[next_i][next_j] not in char2options.keys():
        return None, None, False
    if not _possible(matrix[next_i][next_j], next_i, next_j, i, j):
        return None, None, False
    return next_i, next_j, True

start_i, start_j = None, None
for i in range(m):
    if start_i is not None:
        break
    for j in range(n):
        if matrix[i][j] == 'S':
            start_i, start_j = i, j
            break

ans = 0
for c in char2options.keys():
    matrix[start_i][start_j] = c
    i, j, ok = go(start_i, start_j, None, None)
    prev_i, prev_j = start_i, start_j
    steps = 1
    while ok and (i, j) != (start_i, start_j):
        next_i, next_j, ok = go(i, j, prev_i, prev_j)
        steps += 1
        prev_i, prev_j = i, j
        i, j = next_i, next_j
    if ok and (i, j) == (start_i, start_j):
        ans = steps // 2
print(ans)
