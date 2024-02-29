def topological(G):
    n = len(G)
    visited = [False] * n
    result = []

    def DFS(G, s):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                DFS(G, v)

        result.append(s)

    for i in range(n):
        if not visited[i]:
            DFS(G, i)

    result.reverse()

    return result

graph=[[1,4],
       [3],
       [0,1,4],
       [4],
       []]

print(topological(graph))