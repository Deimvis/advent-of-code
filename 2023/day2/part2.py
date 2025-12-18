
ans = 0
with open('input.txt') as f:
    for line in f:
        meta, sets = line.split(':')
        game_id = int(meta[len('Game '):].strip())
        from collections import defaultdict
        color2min = defaultdict(int)
        for s in sets.split(';'):
            for color_info in s.split(','):
                number, color = map(lambda s: s.strip(), color_info.split())
                number = int(number)
                color2min[color] = max(color2min[color], number)
        from functools import reduce
        import operator
        ans += reduce(operator.mul, color2min.values(), 1)
print(ans)
