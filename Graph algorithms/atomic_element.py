from collections import deque
from math import inf

def Floyd_Warshal(G):
    n = len(G)
    dist = G[:]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    
    return dist


def atomic(G, s, t, min_dist):
    n = len(G)
    d = Floyd_Warshal(G)

    vertices = []

    for v in range(n):
        for u in range(n):
            if d[v][u] > min_dist:
                vertices.append((v, u))

    new_graph = [[] for _ in range(n**2)]

    for v1, v2 in vertices:
        for u1, u2 in vertices:
            if v1 == u1 and v2 == u2:
                continue

            if v1 == u1 or v2 == u2:
                new_graph[v1 * n + v2].append(u1 * n + u2)
                new_graph[u1 * n + u2].append(v1 * n + v2)

    visited = [False] * n**2

    def BFS(G, s):
        q = deque()
        visited[s] = True
        q.append(s)

        while q:
            u = q.popleft()
            visited[u] = True

            for v in G[u]:
                if not visited[v]:
                    q.append(v)

    BFS(new_graph, s * n + t)

    return visited[t * n + s]


G = [[0, 10, inf, 6, 100, inf],
     [10, 0, 7, inf, 10, 3],
     [inf, 7, 0, 6, inf, 8],
     [6, inf, 6, 0, 15, inf],
     [100, 10, inf, 15, 0, 7],
     [inf, 3, 8, inf, 7, 0]]

print(atomic(G, 0, 5, 11))