from queue import PriorityQueue
from math import inf

def dijkstra(G, s):
    n = len(G)
    q = PriorityQueue()
    parent = [None] * n
    visited = [False] * n
    d = [inf] * n

    d[s] = 0
    q.put((0, s))

    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight
            parent[v] = u
            return True
        
        return False
    

    while not q.empty():
        _, u = q.get()

        for v, weight in G[u]:
            if not visited[v] and relax(u, v, weight):
                q.put((d[v], v))

        visited[u] = True

    return d