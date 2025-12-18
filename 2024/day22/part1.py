
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

MOD = 16777216
def go(x):
    process = lambda y: (x ^ y) % MOD
    x = process(x * 64)
    x = process(x // 32)
    x = process(x * 2048)
    return x


ans = 0
for line in lines:
    d = int(line)
    for _ in range(2000):
        d = go(d)
    ans += d
print(ans)
