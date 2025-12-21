
import sys
lines = [line.strip() for line in sys.stdin]
while len(lines) > 0 and len(lines[-1]) == 0:
    lines.pop()

grid = [[c for c in l.strip()] for l in lines]
m, n = len(grid), len(grid[0])

prev = [c != '.' for c in lines[0]]
ans = 0
for i in range(1, m):
    cur = [False]*n
    for j in range(n):
        if not prev[j]: continue
        if grid[i][j] == '.':
            cur[j] = True
        elif grid[i][j] == '^':
            ans += 1
            if j > 0:
                cur[j-1] = True
            if j < n-1:
                cur[j+1] = True
    prev = cur

print(ans)
