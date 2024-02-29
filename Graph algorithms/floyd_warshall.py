from math import inf

def warshall(G):
    n = len(G)
    dist = [[inf for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0

            elif G[i][j] != 0:
                dist[i][j] = G[i][j]


    for t in range(n):
        for x in range(n):
            for y in range(n):
                if dist[x][y] > dist[x][t] + dist[t][y]:
                    dist[x][y] = dist[x][t] + dist[t][y]

    return dist