def zad4(T):
    n = len(T[0])

    SW = [0 for _ in range(n)]
    SK = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            SW[i] += T[i][j]
            SK[i] += T[j][i]

    maks = 0

    for i in range(n):
        for j in range(n):
            if SK[j]/SW[i] > maks:
                maks = SK[j]/SW[i]
                res = (i,j)

    return res

T = [[1,1,1],
     [1,2,3],
     [2,5,1]]

print(zad4(T))