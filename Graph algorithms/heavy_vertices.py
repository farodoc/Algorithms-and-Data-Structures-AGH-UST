# In addition to length of edges, the graph has vertex costs associated with it. Let us define the
# cost of the path as the sum of the costs of its edges and sum of the costs of the vertices (along
# with the ends). Find the cheapest paths between the starting vertex and all the other vertices.
# Find a solution for directed and undirected graph.

from queue import PriorityQueue
from math import inf

def dijkstra(G, cost, s):
    n = len(G)
    q = PriorityQueue()
    d = [inf] * n

    d[s] = cost[s]
    q.put((d[s], s))

    def relax(u, v, weight):
        if d[v] > d[u] + weight + cost[v]:
            d[v] = d[u] + weight + cost[v]
            return True
        
        return False

    while not q.empty():
        _, u = q.get()

        for v, weight in G[u]:
            if relax(u, v, weight):
                q.put((d[v], v))

    
    return d



undirected_graph = [[[1, 4], [2, 3]],
                    [[0, 4], [3, 6]],
                    [[0, 3], [3, 1], [4, 4], [6, 20]],
                    [[1, 6], [2, 1], [5, 3]],
                    [[2, 4], [6, 5]],
                    [[3, 3], [6, 5]],
                    [[2, 20], [4, 5], [5, 5]]]
undirected_graph_vertices = [5, 4, 1, 2, 5, 4, 3]

print(dijkstra(undirected_graph, undirected_graph_vertices, 0))