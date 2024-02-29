# Public transport in a certain city is quite strangely organized. There is a separate charge for
# each section between two stations. However, the total cost incurred from the start of the journey
# is subtracted from this amount (if it is negative you just pay nothing). We are given a connection
# graph in any representation (undirected, weighted). Find the minimum cost of driving this route.

from queue import PriorityQueue
from math import inf

def weird_fees(G, s):
    n = len(G)
    q = PriorityQueue()
    cost = [inf] * n

    cost[s] = 0
    q.put((0, s))

    def relax(u, v, weight, total_cost):
        if weight <= total_cost:
            actual_weight = 0

        else:
            actual_weight, total_cost = weight - total_cost, weight

        if cost[v] > cost[u] + actual_weight:
            cost[v] = cost[u] + actual_weight
            return True
        
        return False


    while not q.empty():
        total_cost, u = q.get()
        for v, weight in G[u]:
            if relax(u, v, weight, cost[u]):
                q.put((cost[v], v))

    
    return cost


graph = [[(1, 60), (3, 120), (4, 40)],
         [(0, 60), (2, 80)],
         [(1, 80), (4, 100), (7, 70)],
         [(0, 120), (6, 150)],
         [(0, 40), (2, 100), (5, 90)],
         [(4, 90), (6, 60)],
         [(3, 150), (5, 60), (7, 90)],
         [(2, 70), (6, 90)]]

print(weird_fees(graph, 0))