from egzP5btesty import runtests
from math import inf

def bridges(G):
    n = len(G)
    time = 0
    low = [inf] * n
    time_visit = [0] * n
    parent = [None] * n
    visited = [False] * n

    def DFS(G, s):
        nonlocal time
        visited[s] = True
        time_visit[s] = time
        low[s] = time
        time += 1

        for v in G[s]:
            if not visited[v]:
                parent[v] = s
                DFS(G, v)
                low[s] = min(low[s], low[v])

            else:
                if v != parent[s]:
                    low[s] = min(low[s], time_visit[v])

    for i in range(n):
        if not visited[i]:
            DFS(G, i)

    bridge = []

    for i in range(n):
        if time_visit[i] == low[i] and parent[i] is not None:
            bridge.append((i, parent[i]))

    return bridge

def koleje (B):
    max_vertex = 0

    for i in range(len(B)):
        B[i] = (min(B[i][0],B[i][1]), max(B[i][0],B[i][1]))
        max_vertex = max(max_vertex, B[i][0], B[i][1])

    B.sort(key = lambda x:(x[0],x[1]))
    
    G = [[] for _ in range(max_vertex + 1)]
    G[B[0][0]].append(B[0][1])
    G[B[0][1]].append(B[0][0])
    prev = (B[0][0], B[0][1])

    for i in range(1, len(B)):
        if (B[i][0], B[i][1]) != prev:
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])
            prev = (B[i][0], B[i][1])

    arr = bridges(G)

    t = [0 for _ in range(max_vertex + 1)]

    for i in range(len(arr)):
        u, v = arr[i][0], arr[i][1]
        
        if len(G[u]) >= 2:
            t[u] += 1

        if len(G[v]) >= 2:
            t[v] += 1

    cnt = 0
    for i in range(max_vertex + 1):
        if t[i] != 0:
            cnt += 1

    return cnt

runtests ( koleje, all_tests=True )