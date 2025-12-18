
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

m, n = len(lines), len(lines[0])
in_range = lambda x,y: 0 <= x < m and 0 <= y < n

ans = 0
for line in lines:
    res, eq = line.split(':')
    res = int(res)
    nums = [int(x) for x in eq.split()]
    ops = len(nums) - 1
    
    possible = False
    for mask in range(2<<ops):
        cur = nums[0]
        for i in range(ops):
            if mask & (1 << i):
                cur += nums[i+1]
            else:
                cur *= nums[i+1]
        if cur == res:
            possible = True
            break
    if possible:
        ans += res
print(ans)
    