
import sys
lines = [line.rstrip() for line in sys.stdin]
while len(lines) > 0 and len(lines[-1]) == 0:
    lines.pop()

n = len(lines[0].split())
eq_ops = lines[-1].split()
eq_nums = [[] for _ in range(n)]
for i in range(len(lines)-1):
    eq_ind = -1
    space_zone = True
    for j in range(len(lines[i])):
        if lines[i][j].isspace():
            space_zone = True
            continue
        if space_zone:
            eq_ind += 1
            space_zone = False
        # (num_ind, digit_order_key, digit)
        eq_nums[eq_ind].append((j, i, int(lines[i][j])))

ans = 0
for i in range(n):
    op = eq_ops[i]
    nums = []
    nums_ = list(sorted(eq_nums[i]))
    ind_offset = nums_[0][0]
    for num_ind_, _, digit in sorted(eq_nums[i]):
        num_ind = num_ind_ - ind_offset
        if num_ind >= len(nums):
            nums.append(0)
        nums[num_ind] = (nums[num_ind] * 10) + digit
    # print(op, nums)
    
    from functools import reduce
    res = sum(nums) if op == '+' else reduce(lambda cur, v: cur * v, nums, 1)
    ans += res

print(ans)
