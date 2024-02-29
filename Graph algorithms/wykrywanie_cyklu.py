from collections import deque

def BFS(G, s):
    n = len(G)
    q = deque()
    visited = [False] * n
    parent = [None] * n
    
    visited[s] = True
    q.append(s)

    while q:
        u = q.popleft()
        for v in G[u]:
            if visited[v] and parent[u] != v:
                return 1
            
            if not visited[v]:
                visited[v] = 1
                parent[v] = u
                q.append(v)

    return 0
# graph has a cycle
graph1 = [[1, 2, 3], [0, 7], [0, 5], [0, 5], [0, 6, 7], [2, 3, 6], [4, 5], [1, 4]]
print(BFS(graph1, 0))

# graph doesn't have a cycle
graph2 = [[1, 2, 5], [0, 3], [0, 4, 7, 8], [1], [2, 6], [0], [4], [2], [2]]
print(BFS(graph2, 0))