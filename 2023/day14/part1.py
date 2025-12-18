
with open('input.txt') as f:
    matrix = [line.strip() for line in f]

m, n = len(matrix), len(matrix[0])
ans = 0
for j in range(n):
    next_pos = 0
    for i in range(m):
        match matrix[i][j]:
            case 'O':
                ans += m - next_pos
                next_pos += 1
            case '.':
                pass
            case '#':
                next_pos = i+1
print(ans)
