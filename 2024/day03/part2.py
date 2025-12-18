
lines = []
with open('input.txt') as f:
    lines = [line.strip() for line in f]

import re
regexp = re.compile(r"(?P<do>do\(\))|(?P<dont>don't\(\))|(?P<mul>mul\((\d{1,3}),(\d{1,3})\))")
ans = 0
enabled = True
for expr in lines:
    matches = regexp.finditer(expr)
    for m in matches:
        groups = m.groupdict()
        match groups:
            case {'do': str()}:
                enabled = True
            case {'dont': str()}:
                enabled = False
            case {'mul': str() as mul}:
                d1, d2 = int(m[4]), int(m[5])
                if enabled:
                    ans += d1*d2
print(ans)
