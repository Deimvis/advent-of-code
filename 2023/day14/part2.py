from copy import deepcopy

CYCLES = 1000000000

with open('input.txt') as f:
    matrix = [[c for c in line.strip()] for line in f]


def do_cycle(matrix):
    matrix_tmp = deepcopy(template)
    for j in range(n):
        next_pos = 0
        for i in range(m):
            match matrix[i][j]:
                case 'O':
                    matrix_tmp[next_pos][j] = 'O'
                    next_pos += 1
                case '.':
                    pass
                case '#':
                    next_pos = i+1
    matrix = matrix_tmp

    matrix_tmp = deepcopy(template)
    for i in range(m):
        next_pos = 0
        for j in range(n):
            match matrix[i][j]:
                case 'O':
                    matrix_tmp[i][next_pos] = 'O'
                    next_pos += 1
                case '.':
                    pass
                case '#':
                    next_pos = j+1
    matrix = matrix_tmp

    matrix_tmp = deepcopy(template)
    for j in range(n):
        next_pos = m-1
        for i in reversed(range(m)):
            match matrix[i][j]:
                case 'O':
                    matrix_tmp[next_pos][j] = 'O'
                    next_pos -= 1
                case '.':
                    pass
                case '#':
                    next_pos = i-1
    matrix = matrix_tmp

    matrix_tmp = deepcopy(template)
    for i in range(m):
        next_pos = n-1
        for j in reversed(range(n)):
            match matrix[i][j]:
                case 'O':
                    matrix_tmp[i][next_pos] = 'O'
                    next_pos -= 1
                case '.':
                    pass
                case '#':
                    next_pos = j-1
    matrix = matrix_tmp
    return matrix

m, n = len(matrix), len(matrix[0])
template = [[c.replace('O', '.') for c in line] for line in matrix]

prev_matrix = matrix
seen = dict()
hs = lambda mat: tuple(tuple(line) for line in mat)
seen = {hs(prev_matrix): 0}
for cycles_done in range(1, CYCLES+1):
    matrix = do_cycle(prev_matrix)

    key = hs(matrix)
    if key in seen:
        begin_cycle = seen[key]
        cycle_length = cycles_done - begin_cycle
        mat_ind = begin_cycle + ((CYCLES - begin_cycle) % cycle_length)
        result_matrix = matrix
        for _ in range(mat_ind - begin_cycle):
            result_matrix = do_cycle(result_matrix)
        prev_matrix = result_matrix
        break
    seen[key] = cycles_done
    prev_matrix = matrix


ans = 0
for i in range(m):
    for j in range(n):
        if prev_matrix[i][j] == 'O':
            ans += m - i
print(ans)
