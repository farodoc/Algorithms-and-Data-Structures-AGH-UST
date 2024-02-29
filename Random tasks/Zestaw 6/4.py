def skoczek(t, w = 0, k = 0, n = 1):
    t[w][k] = n

    if n == len(t) ** 2:
        return True

    ruchy = [(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,1)]

    for skok in ruchy:
        nextW = w + skok[0]
        nextK = k + skok[1]

        if contains(t, nextW, nextK) and t[nextW][nextK] == 0:
            if skoczek(t, nextW, nextK, n + 1):
                return True

    t[w][k] = 0
    return False

def contains(t, w, k):
    if 0 <= w < len(t[0]) and 0 <= k < len(t[0]):
        return True

    return False

t2 = [[0 for _ in range(6)] for _ in range(6)]

skoczek(t2)

for row in t2:
    print(row)
