
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

SZ = 100

cur = 50
ans = 0
for l in lines:
    d = l[0]
    v = int(l[1:])
    dd = (-1 if d == 'L' else 1)
    if v >= SZ:
        ans += (v//SZ)
        v = v%SZ
    raw_next = cur+dd*v
    if cur != 0 and (raw_next <= 0 or raw_next >= SZ):
        ans += 1
    cur = (raw_next+SZ) % SZ
print(ans)
