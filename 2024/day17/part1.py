
grid = []
with open('input.txt') as f:
    grid = [[c for c in line.strip()] for line in f]

m, n = len(grid), len(grid[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

import re
a = int(re.search(r'\d+', ''.join(grid[0]))[0])
b = int(re.search(r'\d+', ''.join(grid[1]))[0])
c = int(re.search(r'\d+', ''.join(grid[2]))[0])

program = list(map(int, ''.join(grid[4]).split(':')[1].split(',')))

def get_combo(x):
    if 0 <= x <= 3:
        return x
    elif x == 4:
        return a
    elif x == 5:
        return b
    elif x == 6:
        return c
    raise RuntimeError(f'combo operand 7')

output = []
i = 0
while i < len(program):
    opcode = program[i]
    if opcode == 0:
        combo = get_combo(program[i+1])
        a = int(a / (1 << combo))
    elif opcode == 1:
        literal = program[i+1]
        b = b ^ literal
    elif opcode == 2:
        combo = get_combo(program[i+1])
        b = combo % 8
    elif opcode == 3:
        print(output, bin(a))
        if a != 0:
            literal = program[i+1]
            i = literal
            continue
    elif opcode == 4:
        b = b ^ c
    elif opcode == 5:
        combo = get_combo(program[i+1])
        output.append(combo % 8)
    elif opcode == 6:
        combo = get_combo(program[i+1])
        b = int(a / (1 << combo))
    elif opcode == 7:
        combo = get_combo(program[i+1])
        c = int(a / (1 << combo))
    else:
        raise RuntimeError(f'Got unsupported opcode: {opcode}')
    i += 2

print(','.join(map(str, output)))
