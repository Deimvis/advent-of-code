
ans = 0
from collections import defaultdict
d = defaultdict(int)
with open('input.txt') as f:
    for i, line in enumerate(f):
        d[i] += 1
        winning, having = map(lambda c: c.split(), line[line.find(':')+1:].split('|'))
        winning = set(winning)
        matches = 0
        for c in having:
            matches += c in winning
        for incr in range(1, 1+matches):
            d[i+incr] += d[i]
print(sum(d.values()))
