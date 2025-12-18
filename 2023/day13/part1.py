
def process(matrix):
    m, n = len(matrix), len(matrix[0])
    in_range = lambda x, y: 0 <= x < m and 0 <= y < n
    def test(sym):
        for i in range(m):
            for j in range(n):
                i1, j1 = sym(i, j)
                if in_range(i1, j1) and matrix[i][j] != matrix[i1][j1]:
                    return False
        return True

    for col in range(n-1):
        sym = lambda i, j: (i, 2*col+1-j)
        if test(sym):
            return col+1
    for row in range(m-1):
        sym = lambda i, j: (2*row+1-i, j)
        if test(sym):
            return 100*(row+1)

ans = 0
with open('input.txt') as f:
    matrix = []
    for line in f:
        if line.strip() == '':
            res = process(matrix)
            print('->', res)
            ans += res
            matrix = []
            continue
        matrix.append([c for c in line.strip()])
    res = process(matrix)
    print('->', res)
    ans += res
print(ans)
