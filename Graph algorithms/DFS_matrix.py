def DFS(G, s):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    d = [-1] * n

    def DFS_visit(G,u):
        nonlocal time
        time += 1
        visited[u] = True
        d[u] = time

        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                parent[v] = u
                DFS_visit(G, v)

        time += 1

    time = 0

    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)

    return d

graph = [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(DFS(graph, 0))