def krolR(t, k, w = 0, s = 0):
    global sumMin

    if w == 7:
        sumMin = min(sumMin, s + t[w][k])
        return

    if k > 0:
        krolR(t, k - 1, w + 1, s + t[w][k])
    
    krolR(t, k, w + 1, s + t[w][k])

    if k < 7:
        krolR(t, k + 1, w + 1, s + t[w][k])


def krol(t, k):
    global sumMin
    sumMin = 10 ** 10
    krolR(t, k)

    return sumMin
    

t = [[1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [2,2,2,2,2,2,2,3]]

print(krol(t, 0))