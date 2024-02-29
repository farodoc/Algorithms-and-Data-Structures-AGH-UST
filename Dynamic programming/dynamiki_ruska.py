from math import inf

def garek(T):
    n = len(T)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    dp[0][0] = T[0]
    dp[0][1] = max(T[0], T[1])
    dp[0][1] = min(T[0], T[1])

    for i in range(1, n):
        dp[i][i] = T[i]
        dp[i - 1][i] = max(T[i - 1], T[i])

    for l in range(3, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = max(T[i] + min(dp[i + 2][j], dp[i + 1][j - 1]), T[j] + min(dp[i][j - 2], dp[i + 1][j - 1]))

    return dp[0][n - 1]



def password(s):
    n = len(s)
    dp = [0] * n
    dp[0] = 1

    if s[0] == '1' and s[1] == '0':
        dp[1] = 1

    if s[0] == '1' and s[1] != '0':
        dp[1] = 3

    if s[0] == '2' and s[1] == '0':
        dp[1] = 1

    elif s[0] == '2' and s[1] <= '6':
        dp[1] = 3

    if s[0] != '1' and s[0] != '2':
        dp[1] = 2


    for i in range(2, n):
        dp[i] += dp[i - 1]

        if s[i - 1] == '1' and s[i] != '0':
            dp[i] += dp[i - 2]

        

def ferry(T, L):
    n = len(T)

    dp = [[[0 for _ in range(L + 1)] for _ in range(L + 1)] for _ in range(n)]
    dp[0][T[0]][0] = 1
    dp[0][0][T[0]] = 1

    max_capacity = 0

    for i in range(1, n):
        for left in range(L + 1):
            for right in range(L - T[i] + 1):
                if dp[i - 1][left][right]:
                    max_capacity = i + 1
                    dp[i][left][right + T[i]] = 1

        for right in range(L + 1):
            for left in range(L - T[i] + 1):
                if dp[i - 1][left][right]:
                    max_capacity = i + 1
                    dp[i][left + T[i]][right] = 1

    return max_capacity


def swap_string(kawiory, s):
    F = [[inf for _ in range(len(s))] for _ in range(len(kawiory))]
    if s[0] == kawiory[0]:
        F[0][0] = 0

    else:
        F[0][0] = 1

    for i in range(1, len(s)):
        if s[i] == kawiory[0]:
            F[0][i] = i

        else:
            F[0][i] = F[0][i - 1] + 1

    for i in range(1, len(kawiory)):
        if s[0] == kawiory[i]:
            F[i][0] = i

        else:
            F[i][0] = F[i - 1][0] + 1

    
    for j in range(1, len(s)):
        for i in range(1, len(kawiory)):
            if s[j] == kawiory[i]:
                F[i][j] = F[i - 1][j - 1]

            else:
                F[i][j] = min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1]) + 1

    print(*F, sep='\n')
    return F[len(kawiory) - 1][len(s) - 1]


def dywany(N):
    F = [inf] * (N + 1)
    F[0] = 0
    F[1] = 1

    for i in range(2, N + 1):
        j = 1
        while i >= j**2:
            F[i] = min(F[i], F[i - j**2] + 1)
            j += 1

    return F[N]


def pseudo_plot(T, k):
    n = len(T)
    F = [[-inf for _ in range(n)] for _ in range(k)]
    sum = [T[0] for _ in range(n)]
    F[0][0] = T[0]

    for i in range(1, n):
        sum[i] = sum[i - 1] + T[i]
        F[0][i] = sum[i]

    for i in range(1, k):
        for j in range(i, n):
            for m in range(i - 1, j):
                F[i][j] = max(F[i][j], min(F[i - 1][m], sum[j] - sum[m]))
    
    #print(*F, sep='\n')
    return F[k - 1][n - 1]

#ploty wystarczy zmienic min z max
T = [5,10,30,20,15]
k = 3 
print(pseudo_plot(T,k))