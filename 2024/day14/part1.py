

lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = 101, 103
# m, n = 7, 11
in_range = lambda x,y: 0 <= x < m and 0 <= y < n


q = [0]*4
for line in lines:
    import re
    match = re.match(r'p=([^ ]*) v=([^ ]*)', line)
    x0,y0 = map(int, match.group(1).split(','))
    dx,dy = map(int, match.group(2).split(','))
    from math import lcm
    kx = lcm(dx, m)
    ky = lcm(dy, n)
    k = lcm(kx, ky)
    
    steps = 100
    steps = steps % k
    x = (x0 + dx * steps) % m
    if x < 0: x += m
    y = (y0 + dy * steps) % n
    if y < 0: y += n

    if x == m//2 or y == n//2: continue
    q[2*(x > m//2) + (y > n//2)] += 1
print(q[0]*q[1]*q[2]*q[3])
