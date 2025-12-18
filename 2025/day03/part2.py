
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
        if vmax == 9:
            break
    return vmaxind


ans = 0
for l in lines:
    nums = list(map(int, l.strip()))
    res = 0
    offset = 0
    for i in range(12):
        arr = nums[offset:len(nums)-(12-i-1)]
        if len(arr) == 0:
            raise RuntimeError(f'unexpected empty arr ({i=}, {offset=}, {nums=})')
        ind = max_ind(arr)
        res = (res * 10) + arr[ind]
        offset += 1+ind
    ans += res

print(ans)
