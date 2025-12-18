
UNFOLD_DEGREE = 5


memo = None
def reset_memo(imax, jmax, cur_lenmax):
    global memo
    memo = [[[None for _ in range(cur_lenmax+1)] for _ in range(jmax+1)] for _ in range(imax+1)]

def with_memo(func):
    global memo
    def wrapper(i, j, cur_len, info, plan):
        if memo[i][j][cur_len] is None:
            memo[i][j][cur_len] = func(i, j, cur_len, info, plan)
        return memo[i][j][cur_len]
    return wrapper

@with_memo
def go(i, j, cur_len, info, plan):
    if i == len(info):
        if j == len(plan):
            assert cur_len == 0
            return 1
        if j == len(plan)-1 and cur_len == plan[j]:
            return 1
        return 0

    assert i < len(info)
    assert j <= len(plan)
    assert j == len(plan) or cur_len <= plan[j]

    match info[i]:
        case '.':
            if cur_len == 0:
                return go(i+1, j, 0, info, plan)
            elif 0 < cur_len < plan[j]:
                return 0
            else:  # cur_len == plan[j]
                return go(i+1, j+1, 0, info, plan)
        case '#':
            if j == len(plan):
                return 0
            elif cur_len + 1 > plan[j]:
                return 0
            else:
                return go(i+1, j, cur_len+1, info, plan)
        case '?':
            res = 0
            # try '.'
            if cur_len == 0:
                res += go(i+1, j, 0, info, plan)
            elif 0 < cur_len < plan[j]:
                res += 0
            else:  # cur_len == plan[j]
                res += go(i+1, j+1, 0, info, plan)
            # try '#'
            if j == len(plan):
                res += 0
            elif cur_len + 1 > plan[j]:
                res += 0
            else:
                res += go(i+1, j, cur_len+1, info, plan)
            return res
    return 0


ans = 0
with open('input.txt') as f:
    for line in f:
        info, plan = line.split()
        plan = [int(x) for x in plan.split(',')]
        print(f'{line.strip():-^50}')
        info = '?'.join([info]*UNFOLD_DEGREE)
        base_plan = plan[::]
        for _ in range(UNFOLD_DEGREE-1): plan.extend(base_plan)
        reset_memo(len(info), len(plan), len(info))
        res = go(0, 0, 0, info, plan)
        print('->', res)
        ans += res
print(ans)
