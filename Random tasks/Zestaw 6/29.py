def center(p1, p2):
    return ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2, (p1[2] + p2[2])/2)


def dist(p):
    return (p[0]**2 + p[1]**2 + p[2]**2)**0.5

def f(t, r, i, curCenter, cnt):
    if cnt >= 3:
        if dist(curCenter) <= r:
            return True

    if i == len(t):
        return False

    if cnt == 0:
        return f(t, r, i + 1, curCenter, cnt) or f(t, r, i + 1, t[i], cnt + 1)

    return f(t, r, i + 1, curCenter, cnt) or f(t, r, i + 1, center(curCenter, t[i]), cnt + 1)

t = [(0,0,0),(2,0,0),(2,0,0)]

print(f(t, 2, 0, 0, 0))