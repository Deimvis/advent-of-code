

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

left_rotation_cycle = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def is_left_rotation(prev_i, prev_j, i, j, next_i, next_j):
    di1, dj1 = (i - prev_i), (j - prev_j)
    di2, dj2 = (next_i - i), (next_j - j)
    for ind in range(len(left_rotation_cycle)):
        if (di1, dj1) == left_rotation_cycle[ind] and (di2, dj2) == left_rotation_cycle[(ind+1)%len(left_rotation_cycle)]:
            return True
    return False

right_rotation_cycle = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def is_right_rotation(prev_i, prev_j, i, j, next_i, next_j):
    di1, dj1 = (i - prev_i), (j - prev_j)
    di2, dj2 = (next_i - i), (next_j - j)
    for ind in range(len(right_rotation_cycle)):
        if (di1, dj1) == right_rotation_cycle[ind] and (di2, dj2) == right_rotation_cycle[(ind+1)%len(right_rotation_cycle)]:
            return True
    return False

def go_left(prev_i, prev_j, i, j):
    di, dj = (i - prev_i), (j - prev_j)
    for ind in range(len(left_rotation_cycle)):
        if left_rotation_cycle[ind] == (di, dj):
            di2, dj2 = left_rotation_cycle[(ind+1)%len(left_rotation_cycle)]
            return i+di2, j+dj2

def go_right(prev_i, prev_j, i, j):
    di, dj = (i - prev_i), (j - prev_j)
    for ind in range(len(right_rotation_cycle)):
        if right_rotation_cycle[ind] == (di, dj):
            di2, dj2 = right_rotation_cycle[(ind+1)%len(right_rotation_cycle)]
            return i+di2, j+dj2

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

def solve():
    ans = 0
    for c in char2options.keys():
        matrix[start_i][start_j] = c
        i, j, ok = go(start_i, start_j, None, None)
        prev_i, prev_j = start_i, start_j
        next_i, next_j = None, None

        left = 0
        right = 0
        cycle_points = set([(start_i, start_j), (i, j)])
        def move_next():
            nonlocal prev_i, prev_j, i, j, next_i, next_j, ok, left, right, cycle_points
            next_i, next_j, ok = go(i, j, prev_i, prev_j)
            if not ok:
                return
            if is_left_rotation(prev_i, prev_j, i, j, next_i, next_j):
                left += 1
            if is_right_rotation(prev_i, prev_j, i, j, next_i, next_j):
                right += 1
            prev_i, prev_j = i, j
            i, j = next_i, next_j
            cycle_points.add((i, j))


        # Traverse over the loop
        while ok and (i, j) != (start_i, start_j):
            move_next()
        if not ok:
            continue
        move_next()


        seen = [[False for _ in range(n)] for _ in range(m)]
        def dfs(i, j):
            nonlocal seen
            if not in_range(i, j): return 0
            if seen[i][j]: return 0
            if (i, j) in cycle_points: return 0
            seen[i][j] = True
            sz = 1
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                i1, j1 = i + di, j + dj
                sz += dfs(i1, j1)
            return sz

        assert abs(left - right) == 4
        is_left_oriented = left > right
        def traverse_inner():
            nonlocal ans
            if is_left_oriented:
                left_i, left_j = go_left(prev_i, prev_j, i, j)
                ans += dfs(left_i, left_j)
                if is_right_rotation(prev_i, prev_j, i, j, next_i, next_j):
                    di, dj = (i - prev_i), (j - prev_j)
                    inner_i, inner_j = i + di, j + dj
                    ans += dfs(inner_i, inner_j)
            else:
                right_i, right_j = go_right(prev_i, prev_j, i, j)
                ans += dfs(right_i, right_j)
                if is_left_rotation(prev_i, prev_j, i, j, next_i, next_j):
                    di, dj = (i - prev_i), (j - prev_j)
                    inner_i, inner_j = i + di, j + dj
                    ans += dfs(inner_i, inner_j)

        def move_next_with_inner_traversal():
            nonlocal prev_i, prev_j, i, j, next_i, next_j, ok
            next_i, next_j, ok = go(i, j, prev_i, prev_j)
            assert ok
            traverse_inner()
            prev_i, prev_j = i, j
            i, j = next_i, next_j


        # Traverse over loop again and mark all points inside the loop
        while (i, j) != (start_i, start_j):
            move_next_with_inner_traversal()
        move_next_with_inner_traversal()
        break

    return ans

ans = solve()
print(ans)
