
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

def go(cur, i, nums, target):
    if i+1 == len(nums):
        return cur == target
    if go(cur+nums[i+1], i+1, nums, target):
        return True
    if go(cur*nums[i+1], i+1, nums, target):
        return True
    if go(int(str(cur) + str(nums[i+1])), i+1, nums, target):
        return True
    return False

ans = 0
for line in lines:
    res, eq = line.split(':')
    res = int(res)
    nums = [int(x) for x in eq.split()]
    ops = len(nums) - 1
    
    possible = go(nums[0], 0, nums, res)
    if possible:
        ans += res
print(ans)
    