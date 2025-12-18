

l1 = []
l2 = []
with open('input.txt') as f:
    for line in f:
        a, b = map(int, line.split())
        l1.append(a)
        l2.append(b)

from collections import Counter
c2 = Counter(l2)

ans = 0
for x in l1:
    ans += x * c2[x]
print(ans)
