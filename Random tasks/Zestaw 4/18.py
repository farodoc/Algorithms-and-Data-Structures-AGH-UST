def maxPodciag(t):
    n = len(t[0])

    maxSum = -10 ** 7

    for i in range(n):
        sumW = 0
        sumK = 0
        tempDl = 0
        for j in range(n):
            tempDl += 1
            if tempDl <= 10:
                sumW += t[i][j]
                sumK += t[j][i]


            else:
                sumW += t[i][j] - t[i][j-10]
                sumK += t[j][i] - t[j-10][i]
            
            maxSum = max(sumK, sumW, maxSum)

    return maxSum

t = [[-1,-1,1],
     [1,2,-5],
     [-10,-7,15]]

print(maxPodciag(t))
            
