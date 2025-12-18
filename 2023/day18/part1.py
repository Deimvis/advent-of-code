
inner_area = 0
p = 0
curx, cury = 0, 0
with open('input.txt') as f:
    for line in f:
        d, length, color = line.split()
        color = color.strip('()#')
        length = int(length)
        newx, newy = curx, cury
        match d:
            case 'U':
                newy = cury + length
            case 'D':
                newy = cury - length
            case 'L':
                newx = curx - length
            case 'R':
                newx = curx + length
        p += length
        inner_area += (curx*newy - cury*newx)  # Shoelace formula
        curx, cury = newx, newy

ans = (abs(inner_area)+p)//2+1
print(ans)
