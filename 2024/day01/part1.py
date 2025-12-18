

l1 = []
l2 = []
with open('input.txt') as f:
    for line in f:
        a, b = map(int, line.split())
        l1.append(a)
        l2.append(b)

l1.sort()
l2.sort()

ans = 0
for x, y in zip(l1, l2):
    ans += abs(x-y)
print(ans)
