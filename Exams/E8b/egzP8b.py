from egzP8btesty import runtests
from math import inf

def warshall(G):
    n = len(G)

    G2 = [[inf for _ in range(n)] for _ in range(n)]

    for u in range(n):
        for v, weight in G[u]:
            G2[u][v] = weight

    for t in range(n):
        for x in range(n):
            for y in range(n):
                if G2[x][y] > G2[x][t] + G2[t][y]:
                    G2[x][y] = G2[x][t] + G2[t][y]

    return G2


def robot( G, P ):
    n = len(G)

    G3 = warshall(G)
    res = 0

    for i in range(1, len(P)):
        res += G3[P[i-1]][P[i]]
    

    return res
    
runtests(robot, all_tests = True)
