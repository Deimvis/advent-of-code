
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

from collections import defaultdict
profit = defaultdict(lambda: 0)

MOD = 16777216
def go(x, diffs, seen):
    process = lambda y: (x ^ y) % MOD
    prev = x
    x = process(x * 64)
    x = process(x // 32)
    x = process(x * 2048)
    diffs.append((x%10)-(prev%10))
    if len(diffs) >= 4:
        if len(diffs) > 4:
            diffs = diffs[1:]
        if tuple(diffs) not in seen:
            seen.add(tuple(diffs))
            profit[tuple(diffs)] += (x%10)
    return x, diffs, seen


for line in lines:
    d = int(line)
    diffs = []
    seen = set()
    for _ in range(2000):
        d, diffs, seen = go(d, diffs, seen)

ans = max(profit.values())
print(ans)
