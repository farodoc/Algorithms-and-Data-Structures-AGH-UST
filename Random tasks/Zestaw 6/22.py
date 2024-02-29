def f(t,i = 0, cnt = 0):
    global stop
    global res
    t2 = [t[i] for i in range(len(t))]

    if stop or i >= len(t):
        return

    if i == len(t) - 1:
        stop = True
        res = cnt
        return

    for p in range(2, int(t[i] ** 0.5) + 2):
        if t2[i] % p == 0 and p != t[i]:
            t2[i] /= p
            f(t, i + p, cnt + 1)


def zad22(t):
    f(t)
    return res

stop = False
res = -1

t = [6,12,5,4,1,1]

print(zad22(t))