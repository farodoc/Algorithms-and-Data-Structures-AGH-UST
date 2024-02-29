from queue import PriorityQueue
from math import inf

def super_cool_paths(G, s):
    n = len(G)
    q = PriorityQueue()
    parent = [None] * n
    d = [inf] * n
    vertices = [inf] * n

    d[s] = 0
    vertices[s] = 0

    q.put((0, s))

    def relax(u, v, dist):
        if d[v] > d[u] + dist:
            d[v] = d[u] + dist
            vertices[v] = vertices[u] + 1
            parent[v] = u
            return True

        elif d[v] == d[u] + dist:
            if vertices[v] > vertices[u] + 1:
                vertices[v] = vertices[u] + 1
                parent[v] = u
                return True
        
        return False

    while not q.empty():
        dist, u = q.get()

        for v in G[u]:
            if relax(u, v[0], v[1]):
                q.put((d[v[0]],v[0]))

    return d, parent, vertices



graph = [[(1, 1), (5, 1), (7, 2)],
         [(0, 1), (2, 1)],
         [(1, 1), (3, 1)],
         [(2, 1), (4, 1)],
         [(3, 1), (6, 1), (7, 2)],
         [(0, 1), (6, 2)],
         [(5, 2), (4, 1)],
         [(0, 2), (4, 2)]]

distance, parent, vertices_length = super_cool_paths(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i], vertices_length[i])
    i -= 1