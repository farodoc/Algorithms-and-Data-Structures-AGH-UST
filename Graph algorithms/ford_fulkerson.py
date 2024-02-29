from collections import deque
from math import inf

def bfs(G, s, t, parent):
    n = len(G)
    visited = [False] * n
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()

        for i in range(n):
            if G[v][i] != 0 and not visited[i]:
                parent[i] = v
                visited[i] = True
                q.append(i)
    
    return visited[t]

def ford_fulkerson(G, s, t):
    n = len(G)
    max_flow = 0
    parent = [None] * n

    while bfs(G, s, t, parent):
        curr_flow = inf
        v = t

        while v != s:
            curr_flow = min(curr_flow, G[parent[v]][v])
            v = parent[v]

        v = t

        while v != s:
            G[parent[v]][v] -= curr_flow
            G[v][parent[v]] += curr_flow
            v = parent[v]

        max_flow += curr_flow

    return max_flow