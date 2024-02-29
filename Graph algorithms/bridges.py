def bridge(G):
    n = len(G)
    visited = [False] * n
    d = [i for i in range(n)]
    parent = [None] * n

    def DFS(G, s):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                parent[v] = s
                DFS(G, v)
                d[s] = min(d[s], d[v])

            elif parent[s] != v:
                d[s] = min(d[s], d[v])

    edges = []

    for i in range(n):
        if not visited[i]:
            DFS(G, i)

    for i in range(n):
        if d[i] == i and parent[i] is not None:
            edges.append((parent[i], i))

    return edges

graph = [[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]
bridge(graph)

print(bridge(graph))