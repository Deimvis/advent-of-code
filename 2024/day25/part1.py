
with open('input.txt') as f:
    data = f.read()
    items = [[[c for c in row] for row in item.split('\n')] for item in data.split('\n\n')]

total_height = len(items[0])
locks = []
keys = []

for item in items:
    is_lock = True
    for c in item[0]:
        if c != '#':
            is_lock = False
            break
    heights = [] 
    if is_lock:
        for col in range(len(item[0])):
            h = 0
            for row in range(len(item)):
                if item[row][col] == '.':
                    break
                h += 1
            heights.append(h-1)
        locks.append(heights)
    else:
        for col in range(len(item[0])):
            h = 0
            for row in reversed(range(len(item))):
                if item[row][col] == '.':
                    break
                h += 1
            heights.append(h-1)
        keys.append(heights)
    ans = 0

for l in locks:
    for k in keys:
        assert len(l) == len(k)
        match = True
        for i in range(len(l)):
            if l[i] + k[i] + 2 > total_height:
                match = False
                break
        ans += match
print(ans)
