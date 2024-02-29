# We are given a graph, in which the vertices are cities and the edges are roads between them. We know
# the fuel price in per liter for each city and the length in kilometers for each road. Our car has
# a 100 liter tank and burns one liter per kilometer. We start from city_A with an empty tank. What is
# the minimum cost that we have to pay for fuel to get to the city_B?

from queue import PriorityQueue
from math import inf

def refueling(G, a, b, tank):
    n = len(G)
    d = [[inf] * (tank + 1) for _ in range(n)]
    q = PriorityQueue()
    visited = [False] * n

    costs = [G[i][1] for i in range(n)]

    for i in range(tank + 1):
        d[a][i] = i * costs[a]

    q.put((0, a))

    def relax(u, v, dist):
        for i in range(dist, tank + 1):
            for j in range(i - dist, tank + 1):
                d[v][j] = min(d[v][j], d[u][i] + j * costs[v])

    while not q.empty():
        _, u = q.get()
        for v in G[u][0]:
            t, dist = v
            if not visited[t]:
                if dist <= tank:
                    relax(u, t, dist)
                    q.put((d[t][dist], t))
            
        visited[u] = True
    
    print(d)

    return min(d[b])



G =[
    [[(1,7),(3,10),(5,30)], 20],
    [[(0,7),(3,8),(2,14)],3],
    [[(1,14),(3,9),(4,15)],100],
    [[(0,10),(1,8),(2,9),(4,20),(5,5)],5],
    [[(2,15),(3,20),(5,15)],5],
    [[(0,30),(3,5),(4,15)],10]
]

print(refueling(G, 0,4, 30))