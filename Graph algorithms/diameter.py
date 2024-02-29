def diameter(edges):
    max_vertex = 0

    for i in range(len(edges)):
        max_vertex = max(max_vertex, max(edges[i]))

    graph = [[] for _ in range(max_vertex + 1)]

    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])

    visited = [False] * len(graph)
    d = [0] * len(graph)

    def DFS_visit(G, s):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                d[v] = d[s] + 1
                DFS_visit(G, v)

    DFS_visit(graph, 0)

    max_idx = d.index(max(d))

    for i in range(len(graph)):
        visited[i] = False
        d[i] = 0

    DFS_visit(graph, max_idx)

    return max(d)


edges = [[0, 1], [0, 2], [0, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [4, 9], [5, 10], [7, 11],
         [7, 12], [7, 13], [8, 14], [8, 15], [11, 16], [11, 17], [13, 18], [16, 19], [19, 20]]
print(diameter(edges))