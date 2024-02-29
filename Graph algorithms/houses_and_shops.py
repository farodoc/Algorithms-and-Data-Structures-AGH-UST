# We have a map of city where are houses and shops. There are also roads (each of length 1)
# that connect a house with a house or a house with a shop. We have to find for each home
# the distance to the nearest shop.

from collections import deque

def bfs(roads, shops):
    max_vertex = 0
    for i in range(len(roads)):
        max_vertex = max(max_vertex, roads[i][0], roads[i][1])

    G = [[] for _ in range(max_vertex + 1)]

    for i in range(len(roads)):
        G[roads[i][0]].append(roads[i][1])
        G[roads[i][1]].append(roads[i][0])


    visited = [False] * len(G)
    d = [0] * len(G)
    q = deque()

    for i in range(len(shops)):
        q.append((shops[i], 0))

    while q:
        u, dist = q.popleft()
        visited[u] = True
    
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = dist + 1
                q.append((v, d[v]))

    return d




roads = [[0, 1], [0, 2], [0, 3], [1, 3], [1, 4], [1, 5], [2, 5], [2, 6], [2, 7], [3, 6], [3, 8],
         [4, 8], [4, 5], [5, 7], [6, 7], [8, 9], [9, 10], [9, 11], [10, 13], [11, 12], [12, 13]]
shops = [2, 3, 9]

print(bfs(roads, shops))