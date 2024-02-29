from queue import PriorityQueue
from math import inf

def prim(G):
    n = len(G)
    visited = [False] * n
    d = [inf] * n
    parent = [None] * n
    q = PriorityQueue()
    d[0] = 0
    q.put((d[0],0))
    
    while not q.empty():
        _, u = q.get()
        visited[u] = True

        for v, edge in G[u]:
            if not visited[v]:
                 if d[v] > edge:
                     d[v] = edge
                     parent[v] = u
                     q.put((d[v],v))
    

    MST=[]

    for i in range(n):
        if parent[i] != None:
             MST.append([parent[i],i,d[i]])
    
    return MST

G = [[(1,15),(3,8),(4,12)],
     [(0,15),(3,11),(4,7)],
     [(3,3),(4,8)],
     [(0,8),(1,11),(2,3),(4,14)],
     [(0,12),(1,7),(2,8),(3,14)]]

print(prim(G))