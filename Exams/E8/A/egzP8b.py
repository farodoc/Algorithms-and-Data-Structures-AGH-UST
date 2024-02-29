from egzP8btesty import runtests
from math import inf

def warshall(G):
    n = len(G)
    dist = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0

            elif G[i][j] != inf:
                dist[i][j] = G[i][j]


    for t in range(n):
        for x in range(n):
            for y in range(n):
                if dist[x][y] > dist[x][t] + dist[t][y]:
                    dist[x][y] = dist[x][t] + dist[t][y]

    return dist


def robot( G, P ):
    G2 = [[inf for _ in range(len(G))] for _ in range(len(G))]

    for u in range(len(G)):
        for v, weight in G[u]:
            G2[u][v] = weight

    
    G2 = warshall(G2)

    cost = 0

    for i in range(1, len(P)):
        cost += G2[P[i - 1]][P[i]]


    return cost
    
runtests(robot, all_tests = True)