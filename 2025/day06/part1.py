
import sys
lines = [line.strip() for line in sys.stdin]
while len(lines) > 0 and len(lines[-1]) == 0:
    lines.pop()

rows = [l.split() for l in lines]
n = len(rows[0])
for i in range(len(rows)-1):
    rows[i] = list(map(int, rows[i]))

ans = 0
for i in range(n):
    op = rows[-1][i]
    cur = (0 if op == '+' else 1)
    for j in range(len(rows)-1):
        v = rows[j][i]
        if op == '+':
            cur += v
        else:
            cur *= v
    ans += cur

print(ans)
