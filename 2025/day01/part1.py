
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

cur = 50
ans = 0
for l in lines:
    d = l[0]
    v = int(l[1:])
    dd = (-1 if d == 'L' else 1)
    cur = (cur+dd*v+100) % 100
    if cur == 0:
        ans += 1
print(ans)
