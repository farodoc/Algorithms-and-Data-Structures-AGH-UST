def szachy(t):
    n = len(t[0])
    maxSum = 0

    sumW = [0 for _ in range(n)]
    sumK = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            sumK[i] += t[j][i]
            sumW[i] += t[i][j]

    for w1 in range(n):
        for k1 in range(n):
            for w2 in range(n):
                for k2 in range(n):
                    if k1 == k2 and w1 != w2:
                        tempSum = sumK[k1] + sumW[w1] + sumW[w2] - 2*(t[w1][k1] + t[w2][k2])
                        if tempSum > maxSum:
                            res = ((w1,k1),(w2,k2))
                            maxSum = tempSum

                    if w1 == w2 and k1 != k2:
                        tempSum = sumK[k1] + sumW[k2] + sumW[w1] - 2*(t[w1][k1] + t[w2][k2])
                        if tempSum > maxSum:
                            res = ((w1,k1),(w2,k2))
                            maxSum = tempSum        

                    if w1 != w2 and k1 != k2:
                        tempSum = sumK[k1] + sumK[k2] + sumW[w1] + sumW[w2] - t[w1][k2] - t[w2][k1]
                        if tempSum > maxSum:
                            res = ((w1,k1),(w2,k2))
                            maxSum = tempSum

    return res      
