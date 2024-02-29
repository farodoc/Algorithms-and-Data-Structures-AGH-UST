from math import inf

"""def plates(T, p):
    n = len(T)
    k = len(T[0])

    suma_prefix = [[0 for _ in range(p + 1)] for _ in range(n)]

    for i in range(n):
        for j in range(1, p + 1):
            suma_prefix[i][j] = suma_prefix[i][j - 1] + T[i][j]


    print(suma_prefix, '\n\n')

    F = [[-inf for _ in range(p)] for _ in range(n)]

    for i in range(p):
        F[0][i] = suma_prefix[0][i]


    for s in range(1, n):
        for t in range(p):
            for i in range(p):
                F[s][t] = max(F[s][t], F[s - 1][t - i] + suma_prefix[s][i])

    return F[n - 1][p - 1]



T = [[1,0,2],
     [2,-1,1],
     [1,0,3]]

print(plates(T, 2))"""

def fabric(X, Y, T):
    F = [[0 for _ in range(X + 1)] for _ in range(Y + 1)]

    for x in range(1, X + 1):
        for y in range(1, Y + 1):
            for xi, yi, price in T:
                if xi <= x and yi <= y:
                    F[y][x] = max(F[y][x], 
                                  price + F[y-yi][xi] + F[y-yi][x-xi]
                                  + F[yi][x-xi])
                    
                xi, yi = yi, xi

                if xi <= x and yi <= y:
                    F[y][x] = max(F[y][x], 
                                  price + F[y-yi][xi] + F[y-yi][x-xi]
                                  + F[yi][x-xi])
                    
    return F[Y][X]


T = [(1,2,1),(6,2,4),(5,4,6),(7,3,15)]

print(fabric(7,4,T))