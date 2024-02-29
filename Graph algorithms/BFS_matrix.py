from collections import deque

def BFS(G, s):
    n = len(G)
    queue = deque()
    visited = [False] * n
    parent = [None] * n
    d = [-1] * n

    visited[s] = True
    d[s] = 0
    queue.append(s)

    while queue:
        u = queue.popleft()
        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                queue.append(v)

    return d

graph = [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(BFS(graph, 2))