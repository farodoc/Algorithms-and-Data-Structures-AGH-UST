def czyPrzyjaciolki(a, b):
    digitsA = [False for _ in range(10)]
    digitsB = [False for _ in range(10)]

    while a > 0:
        digitsA[a % 10] = True
        a //= 10

    while b > 0:
        digitsB[b % 10] = True
        b //= 10

    for i in range(10):
        if digitsB[i] != digitsA[i]:
            return False
        
    return True

def condition(t, row, col):
    n = len(t[0])
    con = True

    for i,j in (row, col+1),(row+1, col+1),(row+1, col),(row+1, col-1),(row, col-1),(row-1, col-1),(row-1, col),(row-1, col+1):
        if i >= 0 and i < n and j >= 0 and j < n:
            if not czyPrzyjaciolki(t[row][col], t[i][j]):
                con = False
                break
        
    return con

def ilePrzyjaciolek(t):
    n = len(t)
    cnt = 0

    for i in range(n):
        for j in range(n):
            if condition(t,i,j):
                cnt += 1

    return cnt

t = [[123,3333312],
     [3312,22132]]

print(ilePrzyjaciolek(t))