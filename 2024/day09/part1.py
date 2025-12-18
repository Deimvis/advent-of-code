
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

disk_dense = lines[0]

disk_compact = []
file_id = 0
for i in range(n):
    length = int(disk_dense[i])
    if i & 1:
        disk_compact.append(('.', length))
    else:
        disk_compact.append((file_id, length))
        file_id += 1

ans = 0
ind = 0
i = 0
j = len(disk_compact) - 1
while i < j:
    while i < j and disk_compact[i][0] != '.':
        for _ in range(disk_compact[i][1]):
            ans += ind * disk_compact[i][0]
            ind += 1
        i += 1
    while i < j and disk_compact[j][0] == '.':
        j -= 1
    if not (i < j):
        break
    
    steps = min(disk_compact[i][1], disk_compact[j][1])
    for _ in range(steps):
        ans += ind * disk_compact[j][0]
        ind += 1
    disk_compact[i] = (disk_compact[i][0], disk_compact[i][1]-steps)
    disk_compact[j] = (disk_compact[j][0], disk_compact[j][1]-steps)
    if disk_compact[i][1] == 0:
        i += 1
    if disk_compact[j][1] == 0:
        j -= 1
for _ in range(disk_compact[i][1]):
    ans += ind * disk_compact[i][0]
    ind += 1

print(ans)