from math import inf

def belman_ford(G, s):
    n = len(G)
    d = [inf] * n
    parent = [None] * n

    d[s] = 0

    def relax(u, v):
        if d[v] > d[u] + G[u][v]:
            d[v] = d[u] + G[u][v]
            parent[v] = u
            return True
        
        return False
    

    for _ in range(n - 1):
        relaxed = False
        for u in range(n):
            for v in range(n):
                if G[u][v] != -inf and relax(u, v):
                    relaxed = True

        if not relaxed:
            break


    for u in range(n):
        for v in range(n):
            if G[u][v] != -inf and relax(u, v):
                return None

    return d


graph=[[-inf,3,-inf, 3, 2],
       [-inf,-inf,-7, -inf, -inf],
       [-inf,-inf,-inf, 8, -inf],
       [-inf,-1,-inf, -inf, -2],
       [-inf,-inf,-inf, -inf, -inf]]

print(belman_ford(graph, 0))