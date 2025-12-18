
ans = 0
with open('input.txt') as f:
    for line in f:
        winning, having = map(lambda c: c.split(), line[line.find(':')+1:].split('|'))
        winning = set(winning)
        matches = 0
        for c in having:
            matches += c in winning
        if matches == 0:
            score = 0
        else:
            score = 1 << (matches - 1)
        ans += score
print(ans)
