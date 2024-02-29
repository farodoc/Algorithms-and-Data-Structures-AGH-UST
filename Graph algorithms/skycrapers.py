# The skyscraper has 7 floors and n elevators, but there are no stairs. Each elevator has a list of
# the floors it travels to and the speed in seconds per floor. We are on the i floor and we want to get
# to the j floor. What is the minimum time in seconds that we have to spend in elevators to get there?

from queue import PriorityQueue
from math import inf

def elevators_in_skyscraper(floors, start, end):
    n = len(floors)
    G = [[] for _ in range(n + 1)]

    for i in range(n):
        floors[i][0].sort()

    for i in range(n):
        for j in floors[i][0]:
            G[i].append((j, (j - i) * floors[i][1]))
            G[j].append((i, (j - i) * floors[i][1]))

    def relax(u, v, weight):
        if d[v] > d[u] + weight:
            d[v] = d[u] + weight

    d = [float('inf')] * (n + 1)
    visited = [False] * (n + 1)
    q = PriorityQueue()
    d[start] = 0
    q.put((0, start))

    while q and not visited[end]:
        dist, u = q.get()
        if not visited[u]:
            visited[u] = True
            for v, weight in G[u]:
                if not visited[v]:
                    relax(u, v, weight)
                    q.put((d[v], v))

    
    return d

floors = [[[1, 2, 5], 3],
          [[3, 4, 5], 5],
          [[3, 6], 2],
          [[4], 3],
          [[5], 1],
          [[6], 4]]

print(elevators_in_skyscraper(floors, 1, 5))