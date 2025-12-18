
import sys
lines = [line for line in sys.stdin]


def find_invalids_sum(lb: int, ub: int):
    lb_digits = digits(lb)
    ub_digits = digits(ub)
    n = len(ub_digits)
    lb_digits = [0 for _ in range(n-len(lb_digits))] + lb_digits
    
    ans = 0
    # print('range:', lb_digits, ub_digits)
    def go(cur_digits: list[int], i: int, cur_gt_lb: bool, cur_lt_ub: bool, is_zero: bool):
        # print('go', cur_digits, i, cur_gt_lb)
        nonlocal ans
        if len(cur_digits) > n//2:
            # print('bad len')
            return
        if len(cur_digits) > 0:
            cand = value(cur_digits + cur_digits)
            # print('cand', cand)
            if cand >= lb and cand <= ub:
                # print('found', cand)
                ans += cand
        if i == n:
            return
        mind = lb_digits[i]
        if cur_gt_lb:
            mind = 0
        maxd = ub_digits[i]
        if cur_lt_ub:
            maxd = 9
        for x in range(mind, maxd+1):
            if is_zero and x == 0:
                go([], i+1, False, True, True)
            else:
                go(cur_digits + [x], i+1, cur_gt_lb or (x > mind), cur_lt_ub or (x < maxd), False)

    go([], 0, False, False, True)
    return ans


def digits(v: int) -> list[int]:
    res = []
    while v > 0:
        res.append(v % 10)
        v //= 10
    return list(reversed(res))

def value(digits: list[int]) -> int:
    v = 0
    for x in digits:
        v *= 10
        v += x
    return v

def brute_force(lb: int, ub: int):
    ans = 0
    for x in range(lb, ub+1):
        x_digits = digits(x)
        n = len(x_digits)
        if n % 2 == 0 and x_digits[:n//2] == x_digits[n//2:]:
            print('brute force found', x)
            ans += x
    return ans


ranges = lines[0].strip().split(',')
ranges = list(map(lambda r: (int(r.split('-')[0]), int(r.split('-')[1])), ranges))
ans = 0
# find_invalids_sum(328412,412772)
for r in ranges:
    v = find_invalids_sum(r[0], r[1])
    # v_ = brute_force(r[0], r[1])
    # if v != v_:
    #     raise RuntimeError(f'my: {v}, brute force: {v_}')
    ans += v
print(ans)
