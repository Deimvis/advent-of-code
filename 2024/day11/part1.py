
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]


stones = [int(x) for x in lines[0].split()]

def blink():
    global stones
    result = []
    for x in stones:
        if x == 0:
            result.append(1)
        elif len(str(x))%2==0:
            s = str(x)
            n = len(s)
            result.append(int(s[:n//2]))
            result.append(int(s[n//2:]))
        else:
            result.append(x*2024)
    stones = result
    
    
for _ in range(25):
    blink()

print(len(stones))
