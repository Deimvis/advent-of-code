
import sys
lines = [line for line in sys.stdin]

# returns first ind of value == max(arr)
def max_ind(arr: list[int]) -> int:
    if len(arr) == 0:
        raise RuntimeError('max_ind on empty arr')
    vmax = float('-inf')
    vmaxind = -1
    for i in range(len(arr)):
        if arr[i] > vmax:
            vmax = arr[i]
            vmaxind = i
    return vmaxind


ans = 0
for l in lines:
    nums = list(map(int, l.strip()))
    i1 = max_ind(nums[:-1])
    i2 = max_ind(nums[i1+1:])+i1+1
    res = nums[i1] * 10 + nums[i2]
    ans += res

print(ans)
