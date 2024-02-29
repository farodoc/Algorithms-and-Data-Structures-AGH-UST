def A(x):
    return x + 3

def B(x):
    return 2 * x

def C(x):
    res = 0
    multi = 1

    while x != 0:
        if (x % 10) % 2 == 0:
            res += multi * (x % 10 + 1)
        
        else:
            res += multi * (x % 10)

        multi *= 10
        x //= 10

    return res

def f(x, y, n, cnt, prev):
    if x == y:
        if prev != 'C' and n > cnt:
            return 1 + f(x, y, n, cnt + 1, 'C')
            
        return 1

    if cnt >= n:
        return 0

    if prev == 0:
        return f(A(x), y, n, cnt + 1, 'A') + f(B(x), y, n, cnt + 1, 'B') + f(C(x), y, n, cnt + 1, 'C')

    elif prev == 'A':
        return f(B(x), y, n, cnt + 1, 'B') + f(C(x), y, n, cnt + 1, 'C')

    elif prev == 'B':
        return f(A(x), y, n, cnt + 1, 'A') + f(C(x), y, n, cnt + 1, 'C')

    else:
        return f(A(x), y, n, cnt + 1, 'A') + f(B(x), y, n, cnt + 1, 'B')

print(f(11, 31, 4, 0, 0))