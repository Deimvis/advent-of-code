
import sys
lines = [line.strip() for line in sys.stdin]

grid = lines
m = len(grid)
n = len(grid[0])

in_range = lambda x, y: 0 <= x < m and 0 <= y < n
ans = 0
for i in range(m):
    for j in range(n):
        if lines[i][j] == '@':
            cnt = 0
            import itertools
            for di, dj in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if di == dj == 0: continue
                i1 = i+di
                j1 = j+dj
                cnt += in_range(i1, j1) and lines[i1][j1] == '@'
            if cnt < 4:
                ans += 1
print(ans)
