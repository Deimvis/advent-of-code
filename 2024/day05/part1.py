
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

from collections import defaultdict
must_before = defaultdict(set)
i = 0
while i < len(lines) and len(lines[i]) > 0:
    x, y = map(int, lines[i].split('|'))
    must_before[x].add(y)
    i += 1

updates = lines[i+1:]
ans = 0
for upd in updates:
    pages = list(map(int, upd.split(',')))
    seen = set()
    valid = True
    for p in pages:
        if seen.intersection(must_before[p]):
            valid = False
            break
        seen.add(p)
    if valid:
        ans += pages[len(pages)//2]
print(ans)
