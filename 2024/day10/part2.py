
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n


zeros = []
for i in range(m):
    for j in range(n):
        if lines[i][j] == '0':
            zeros.append((i, j))


cache = {}
def get_rating(i, j):
    if int(lines[i][j]) == 9:
        return 1
    global cache
    if (i, j) not in cache:
        rating = 0
        dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        for di, dj in dirs:
            i1 = i + di
            j1 = j + dj
            if not in_range(i1, j1): continue
            if int(lines[i1][j1]) != int(lines[i][j])+1: continue
            rating += get_rating(i1, j1)
        cache[(i, j)] = rating
    return cache[(i, j)]


ans = 0
for (i, j) in zeros:
    ans += get_rating(i, j)
print(ans)
