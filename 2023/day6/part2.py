
with open('input.txt') as f:
    time_line = f.readline()
    t = int(''.join(time_line[len('Time:'):].split()))
    distance_line = f.readline()
    d = int(''.join(distance_line[len('Distance:'):].split()))

l = 0
r = t//2
while r - l > 1:
    m = l + (r - l) // 2
    if m * (t - m) > d:
        r = m
    else:
        l = m
begin = r

l = t//2
r = t
while r - l > 1 :
    m = l + (r - l) // 2
    if m * (t - m) > d:
        l = m
    else:
        r = m
end = l + 1

ans = end - begin
print(ans)
