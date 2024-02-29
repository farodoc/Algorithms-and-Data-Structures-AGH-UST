class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0


def find(x):
    i = 0
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    
    if x.rank < y.rank:
        x.parent = y

    else:
        y.parent = x
        if x.rank == y.rank:
            x.rank += 1

    return True


def kruskal(G):
    n = len(G)
    edges = []
    MST = []

    for u in range(n):
        for v, weight in G[u]:
            edges.append([u, v, weight])

    edges.sort(key=lambda x: x[2])

    V = [Node(i) for i in range(n)]

    for edge in edges:
        u, v, weight = edge
        if union(V[u], V[v]):
            MST.append([u, v, weight])

    return MST

G = [[(1,15),(3,8),(4,12)],
     [(0,15),(3,11),(4,7)],
     [(3,3),(4,8)],
     [(0,8),(1,11),(2,3),(4,14)],
     [(0,12),(1,7),(2,8),(3,14)]]

print(kruskal(G))