
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
grid = [[lines[i][j] for j in range(n)] for i in range(m)]

in_range = lambda x,y: 0 <= x < m and 0 <= y < n

target = 'MAS'
def eq_mas(i, j, d):
    i = i - d[0]
    j = j - d[1]
    for step in range(3):
        if not in_range(i,j): return False
        if grid[i][j] != target[step]: return False
        i += d[0]
        j += d[1]
    return True
        

def is_xmas(i, j):
    first_diag = (eq_mas(i, j, [-1, -1]) or eq_mas(i, j, [1, 1]))
    second_diag = (eq_mas(i, j, [-1, 1]) or eq_mas(i, j, [1, -1]))
    return first_diag and second_diag

ans = 0
for i in range(m):
    for j in range(n):
        ans += is_xmas(i, j)
print(ans)
