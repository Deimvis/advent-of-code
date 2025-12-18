
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

disk_dense = lines[0]

disk_compact = []
file_id = 0
offset = 0
for i in range(n):
    length = int(disk_dense[i])
    if i & 1:
        disk_compact.append(('.', length, offset))
    else:
        disk_compact.append((file_id, length, offset))
        file_id += 1
    offset += length

ans = 0
ind = 0
i = 0
j = len(disk_compact) - 1
while j >= 0:
    while j >= 0 and disk_compact[j][0] == '.':
        j -= 1
    if not (j > 0):
        break
    
    file_id = disk_compact[j][0]
    file_length = disk_compact[j][1]
    
    moved = False
    for i in range(j):
        if disk_compact[i][0] == '.' and disk_compact[i][1] >= file_length:
            offset = disk_compact[i][2]
            for ind in range(offset, offset+file_length):
                ans += ind * file_id
            
            disk_compact[i] = (disk_compact[i][0], disk_compact[i][1]-file_length, disk_compact[i][2]+file_length)
            moved = True
            break
            
    if not moved:
        file_offset = disk_compact[j][2]
        for ind in range(file_offset, file_offset+file_length):
            ans += ind * file_id
    
    j -= 1
print(ans)