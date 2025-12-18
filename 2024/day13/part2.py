
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
    ax, ay = parse_rec(lines[machine*4], '+')
    bx, by = parse_rec(lines[machine*4+1], '+')
    prize = parse_rec(lines[machine*4+2], '=')
    maxx = prize[0]
    maxy = prize[1]
    
    maxx += 10000000000000
    maxy += 10000000000000

    if ax*by == ay*bx:
        raise RuntimeError('corner case')
    qa = (bx*maxy - by*maxx) / (ay*bx - ax*by)
    qb = (maxx - qa*ax) / bx
    tol = 1e-3
    qa_ = int(round(qa))
    qb_ = int(round(qb))
    if abs(qa - qa_) < tol and abs(qb-qb_) < tol:
        ans += 3*qa_ + qb_

print(ans) 
