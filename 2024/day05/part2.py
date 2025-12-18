
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

from functools import cmp_to_key
updates = lines[i+1:]
ans = 0
for upd in updates:
    pages = list(map(int, upd.split(',')))
    seen = set()
    invalid = False
    for p in pages:
        if seen.intersection(must_before[p]):
            invalid = True
            break
        seen.add(p)
    if invalid:
        def cmp(x, y):
            if x in must_before[y]:
                return -1
            if y in must_before[x]:
                return 1
            return 0
        pages.sort(key=cmp_to_key(cmp))
        ans += pages[len(pages)//2]
print(ans)
