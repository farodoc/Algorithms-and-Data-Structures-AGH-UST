def DFS(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    d = [-1] * n

    def DFS_visit(G, u):
        nonlocal time
        time += 1
        visited[u] = True
        d[u] = time

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(G, v)

        time += 1


    time = 0

    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)

    return d

G = [[1],[0,2],[1,3],[2,4],[3]]
print(DFS(G,0))