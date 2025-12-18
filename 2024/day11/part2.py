
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]


from collections import defaultdict
stones = defaultdict(int)
for x in map(int, lines[0].split()): stones[x] += 1 

def blink():
    global stones
    result = defaultdict(int)
    for x, cnt in stones.items():
        if x == 0:
            result[1] += cnt
        elif len(str(x))%2==0:
            s = str(x)
            n = len(s)
            result[int(s[:n//2])] += cnt
            result[int(s[n//2:])] += cnt
        else:
            result[x*2024] += cnt
    stones = result 
    
for i in range(75):
    blink()

print(sum(stones.values()))
