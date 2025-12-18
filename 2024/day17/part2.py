
grid = []
with open('input.txt') as f:
    grid = [[c for c in line.strip()] for line in f]

m, n = len(grid), len(grid[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

# import re
# a = int(re.search(r'\d+', ''.join(grid[0]))[0])
# b = int(re.search(r'\d+', ''.join(grid[1]))[0])
# c = int(re.search(r'\d+', ''.join(grid[2]))[0])

program = list(map(int, ''.join(grid[4]).split(':')[1].split(',')))


def run_iteration(a, b, c) -> int:
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

    result = None
    for i in range(0, len(program), 2):
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
            break
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            combo = get_combo(program[i+1])
            result = combo % 8
        elif opcode == 6:
            combo = get_combo(program[i+1])
            b = int(a / (1 << combo))
        elif opcode == 7:
            combo = get_combo(program[i+1])
            c = int(a / (1 << combo))
        else:
            raise RuntimeError(f'Got unsupported opcode: {opcode}')
    return result


candidates = [0]
for exp in reversed(program):
    next_candidates = []
    for cand in candidates:
        for inc in range(1 << 3):
            a = (cand << 3) + inc
            if a == 0: continue
            act = run_iteration(a, 0, 0)
            if act == exp:
                next_candidates.append(a)
    candidates = next_candidates
print(min(candidates))
