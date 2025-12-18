
ans = 0
with open('input.txt') as f:
    for line in f:
        first = None
        last = None
        for c in line:
            if c.isdigit():
                if first is None:
                    first = c
                last = c
        ans += int(first + last)
print(ans)
