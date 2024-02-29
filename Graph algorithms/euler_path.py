def euler(G):
    path = []

    def DFS(G, s):
        for i in range(len(G)):
            if G[s][i] == 1:
                G[s][i] = 0
                G[i][s] = 0
                DFS(G, i)
        
        path.append(s)

    DFS(G, 0)
    return path

graph = [[0, 1, 1, 0, 0, 0],
         [1, 0, 1, 1, 0, 1],
         [1, 1, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [0, 1, 1, 1, 1, 0]]

print(euler(graph))