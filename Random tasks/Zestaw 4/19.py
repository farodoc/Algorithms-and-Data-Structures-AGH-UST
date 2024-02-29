def liczbaPar(t, w, k, iloczyn):
    n = len(t[0])
    cnt = 0

    for i,j in (w+1,k+2),(w-1,k+2),(w-2,k+1),(w-2,k-1),(w-1,k-2),(w+1,k-2),(w+2,k-1),(w+2,k+1):
        if i >= 0 and i < n and j >= 0 and j < n:
            if t[w][k] * t[i][j] == iloczyn:
                cnt += 1
    
    return cnt

def zad19(t,iloczyn):
    n = len(t[0])
    cnt = 0

    for w in range(n):
        for k in range(n):
            cnt += liczbaPar(t,w,k,iloczyn)

    return cnt/2

t = [[2,2,4],
     [5,0,10],
     [2,4,4]]

print(int(zad19(t,20)))