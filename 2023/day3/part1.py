
with open('input.txt') as f:
    matrix = f.read().strip().split('\n')

m, n = len(matrix), len(matrix[0])
in_range = lambda x, y: 0 <= x < m and 0 <= y < n
seen_number = [[False for _ in range(n)] for _ in range(m)]

def parse_num(i, j):
    assert matrix[i][j].isdigit()
    left = j
    right = j
    while left-1 >= 0 and matrix[i][left-1].isdigit():
        left -= 1
    while right+1 < n and matrix[i][right+1].isdigit():
        right += 1
    for j in range(left, right+1):
        seen_number[i][j] = True
    return int(matrix[i][left:right+1])


ans = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] != '.' and not matrix[i][j].isdigit():
            import itertools
            for di, dj in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if di == dj == 0: continue
                i1 = i + di
                j1 = j + dj
                if in_range(i1, j1) and matrix[i1][j1].isdigit() and not seen_number[i1][j1]:
                    ans += parse_num(i1, j1)
print(ans)
