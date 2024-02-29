def best_sum(T, S):
    n = len(T)
    tab = [[T[i][0], T[i][1], S[i]] for i in range(n)]

    tab.sort(key = lambda x:x[0])

    F = [tab[i][2] for i in range(n)]

    for i in range(1, n):
        for j in range(i):
            if tab[i][0] > tab[j][1]:
                F[i] = max(F[i], tab[i][2] + F[j])

    return F



T = [(2,5),(7,10),(1,6),(0,1),(6,8),(11,12),(7,12)]
S = [7,6,13,8,4,1,15]

print(best_sum(T,S))