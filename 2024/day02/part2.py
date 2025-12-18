
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]


def is_safe(nums):
    incr = nums[1] > nums[0]
    for i in range(1, len(nums)):
        if not (1 <= abs(nums[i] - nums[i-1])  <= 3):
            return False
        if not (incr ^ (nums[i] - nums[i-1] < 0)):
            return False
    return True


safe = 0
for line in lines:
    nums = list(map(int, line.split()))
    cur_safe = False
    cur_safe |= is_safe(nums)
    for i in range(len(nums)):
        cur_safe |= is_safe(nums[:i] + nums[i+1:])
    safe += cur_safe
print(safe)
