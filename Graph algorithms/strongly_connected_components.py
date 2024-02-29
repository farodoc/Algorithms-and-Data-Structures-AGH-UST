def SCC(G):
    n = len(G)
    visited = [False] * n
    order = []

    def DFS(G, s, arr):
        visited[s] = True
        for v in G[s]:
            if not visited[v]:
                DFS(G, v, arr)

        arr.append(s)

    for i in range(n):
        if not visited[i]:
            DFS(G, i, order)

    def swap_edges(G):
        G2 = [[] for _ in range(n)]

        for v in range(n):
            for u in G[v]:
                G2[u].append(v)

        return G2
    
    G2 = swap_edges(G)

    components = []
    visited = [False] * n

    for v in order:
        temp_components = []
        if not visited[v]:
            DFS(G, v, temp_components)
            components.append(temp_components)

    return components

G = [[1], [2], [0, 3, 8], [4, 6], [5], [3], [5], [8], [9], [5, 10], [3, 7]]

print(SCC(G))