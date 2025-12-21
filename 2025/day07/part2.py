
import sys
lines = [line.strip() for line in sys.stdin]
while len(lines) > 0 and len(lines[-1]) == 0:
    lines.pop()

grid = [[c for c in l.strip()] for l in lines]
m, n = len(grid), len(grid[0])

prev = [1 if c != '.' else 0 for c in lines[0]]
ans = 0
for i in range(1, m):
    cur = [0]*n
    for j in range(n):
        if not prev[j]: continue
        if grid[i][j] == '.':
            cur[j] += prev[j]
        elif grid[i][j] == '^':
            ans += 1
            if j > 0:
                cur[j-1] += prev[j]
            if j < n-1:
                cur[j+1] += prev[j]
    prev = cur

print(sum(prev))
