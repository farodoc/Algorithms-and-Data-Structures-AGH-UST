def eulerian(G):
    n = len(G)

    for i in range(n):
        edges = 0
        for j in range(n):
            if G[i][j] == 1:
                edges += 1

        if edges % 2 == 1:
            return False
        
    path = []

    def DFS(G, s):
        for i in range(n):
            if G[s][i] == 1:
                G[s][i], G[i][s] = 0, 0
                DFS(G, i)

        path.append(s)

    DFS(G, 0)
    path.reverse()

    return path

G = [[0,1,1,0,0,0],
     [1,0,1,0,0,0],
     [1,1,0,1,0,1],
     [0,0,1,0,1,0],
     [0,0,0,1,0,1],
     [0,0,1,0,1,0]]

print(eulerian(G))