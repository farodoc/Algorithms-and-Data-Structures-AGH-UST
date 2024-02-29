def f(n, pionki, w, k, cnt):
    global steps

    if w == n - 1 and k == n - 1:
        steps = min(steps, cnt)

    krok = 1
    while krok + w < n:
        if(krok + w, k) in pionki:
            break

        f(n, pionki, w + krok, k, cnt + 1)
        krok += 1

    krok = 1
    while krok + k < n:
        if(w, k + krok) in pionki:
            break

        f(n, pionki, w, k + krok, cnt + 1)
        krok += 1

def rook(N, L):
    global steps
    steps = 10 ** 10
    f(N, L, 0, 0, 0)

    if steps == 10**10:
        return None
    
    return steps

print(rook(8, [(0,2), (4,0), (6,4)]))
