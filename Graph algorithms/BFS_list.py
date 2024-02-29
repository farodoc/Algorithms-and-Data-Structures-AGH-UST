from collections import deque

def BFS(G, s):
    n = len(G)
    queue = deque()
    visited = [False] * n
    d = [-1] * n
    parent = [None] * n

    visited[s] = True
    d[s] = 0
    queue.append(s)
    while queue:
        u = queue.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
                queue.append(v)
    
    return d

G = [[1,3],[0,2],[1,5],[0,4,6],[3,5],[2,4,6],[3,5]]

print(BFS(G,0))