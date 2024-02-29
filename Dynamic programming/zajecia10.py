#Najdluzszy wspolny podciag, tablica A o dlugosci n i tablica B o dlugosci n
#         {f(i-1,j-1) + 1,   A[i] == B[j]
#f(i,j) = {max(f(i-1,j), f(i,j-1)),  A[i] != B[j]
n = 100

def f(i,j):
    d = [[0 for i in range(n + 1)] for j in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(A[i] == B[j]):
                d[i][j] = d[i-1][j-1] + 1

            else:
                d[i][j] = max(d[i-1][j], d[i][j-1])
    
    return d[n][n]