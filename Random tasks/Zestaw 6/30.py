def center(p1,p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)

def dist(p):
    return (p[0]**2 + p[1]**2)**0.5

def f(t, i, r, k, curCenter, cnt):
    if cnt > 0 and cnt % 3 == 0 and cnt < k:
        if dist(curCenter) <= r:
            return True

    if i == len(t) or cnt >= k:
        return False

    if cnt == 0:
        return f(t, i + 1, r, k, curCenter, cnt) or f(t, i + 1, r, k, t[i], cnt + 1)

    return f(t, i + 1, r, k, curCenter, cnt) or f(t, i + 1, r, k, center(curCenter, t[i]), cnt + 1)

def zad(t, r, k):
    return f(t, 0, r, k, 0, 0)

t = [(0,0), (1,1)]

print(zad(t, 1, 2))