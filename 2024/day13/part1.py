
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

ans = 0
for machine in range((m+1)//4):
    def parse_rec(b, sep):
        diffs = b.split(':')[1].split(',')
        parse_diff = lambda d: int(d[d.index(sep)+1:].strip())
        return parse_diff(diffs[0]), parse_diff(diffs[1])
    a = parse_rec(lines[machine*4], '+')
    b = parse_rec(lines[machine*4+1], '+')
    prize = parse_rec(lines[machine*4+2], '=')
    maxx = prize[0]
    maxy = prize[1]
    in_range = lambda x,y: 0 <= x < maxx+1 and 0 <= y < maxy+1
    from collections import deque
    q = deque([(0, 0, 0)])
    seen = set()
    seen.add((0, 0))
    tokens = float('+inf')
    while q:
        x, y, t = q.popleft()
        if (x, y) == (maxx, maxy):
            tokens = min(tokens, t)
        x1, y1 = x+a[0],y+a[1]
        if in_range(x1, y1) and (x1, y1) not in seen:
            seen.add((x1, y1))
            q.append((x1, y1, t+3))
        x2, y2 = x+b[0],y+b[1]
        if in_range(x2, y2) and (x2, y2) not in seen:
            seen.add((x2, y2))
            q.append((x2, y2, t+1))
    if tokens == float('+inf'):
        continue
    ans += tokens
print(ans) 
