
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

import re
regexp = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
ans = 0
for expr in lines:
    matches = regexp.findall(expr)
    for d1, d2 in matches:
        ans += int(d1)*int(d2)
print(ans)
