def waga(x):
    if x == 0:
        return 0

    cnt = 0
    dzielnik = 2
    while x > 1:
        if x % dzielnik == 0:
            cnt += 1
            while x % dzielnik == 0:
                x /= dzielnik

        dzielnik += 1
    
    return cnt

def funR(t, s1 = 0, s2 = 0, s3 = 0, p = 0):
    if p == len(t):
        return s1 == s2 == s3

    return funR(t, s1 + t[p], s2, s3, p + 1) or funR(t, s1, s2 + t[p], s3, p + 1) or funR(t, s1, s2, s3 + t[p], p + 1)

def fun(t):
    for i in range(len(t)):
        t[i] = waga(t[i])

    return funR(t)

t = [2,2,2,2,2,2]

print(fun(t))