
color2limit = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

ans = 0
with open('input.txt') as f:
    for line in f:
        meta, sets = line.split(':')
        game_id = int(meta[len('Game '):].strip())
        possible = True
        for s in sets.split(';'):
            if not possible: break
            for color_info in s.split(','):
                number, color = map(lambda s: s.strip(), color_info.split())
                number = int(number)
                if number > color2limit[color]:
                    possible = False
                    break
        if possible:
            ans += game_id

print(ans)
