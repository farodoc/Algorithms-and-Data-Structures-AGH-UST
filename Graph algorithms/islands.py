# A certain land consists of islands between which there are air, ferry and bridge connections.
# There is at most one type of connection between two islands. The transport of the overflight from
# island to island transports 8B, ferry crossing transports 5B and for bridge crossing you have to pay 1B.
# Find route from island A to island B which on each subsequent island changes the transport
# to a different one and minimizes the transport of the trip. We are given an array G that specifies
# the transport of connections between the islands. Value 0 means that there is no direct connection.
# Implement islands(G, A, B) function that returns the minimum travels transport from island A
# to island B. If such a route doesn't exist, the function should return None.

from queue import PriorityQueue
from math import inf

def islands(G, A, B):
    n = len(G)
    d = [[inf] * 3 for _ in range(n)]
    q = PriorityQueue()

    for i in range(3):
        d[A][i] = 0

    q.put((0, A, 0))

    def relax(u, v, transport):
        rel = False

        if transport == 1:
            if d[v][0] > d[u][1] + transport:
                d[v][0] = d[u][1] + transport
                rel = True

            if d[v][0] > d[u][2] + transport:
                d[v][0] = d[u][2] + transport
                rel = True
            
            if rel:
                q.put((d[v][0], v, 1))

        elif transport == 5:
            if d[v][1] > d[u][0] + transport:
                d[v][1] = d[u][0] + transport
                rel = True

            if d[v][1] > d[u][2] + transport:
                d[v][1] = d[u][2] + transport
                rel = True
            
            if rel:
                q.put((d[v][1], v, 5))

        else:
            if d[v][2] > d[u][0] + transport:
                d[v][2] = d[u][0] + transport
                rel = True

            if d[v][2] > d[u][1] + transport:
                d[v][2] = d[u][1] + transport
                rel = True
                
            if rel:
                q.put((d[v][2], v, 8))


    while not q.empty():
        _, u, prev= q.get()

        for v in range(n):
            if G[u][v] != 0 and G[u][v] != prev:
                relax(u, v, G[u][v])


    return d[B]


G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 1, 0, 5],
     [0, 0, 8, 1, 0, 5, 0]]

print(islands(G, 5, 2))