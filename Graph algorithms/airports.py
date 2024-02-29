# We are given a list of threes (city_A, city_B, cost). Each of them means that we can build a road
# between city_A and city_B for the given cost. Moreover in any city we can build an airport at a K cost,
# independent of the city. At the beginning, there is no airport in any city, nor is there a road built
# between any two cities. Our goal is to build airports and roads for a minimum total cost so that every
# city has access to the airport. The city has access to the airport if:
#   1) it has an airport
#   2) it is possible to travel to another city which has an airport
# If there is more than one solution with the minimum cost, choose the one with the most airports.

class Node:
    def __init__(self, val):
        self.val = val
        self.rank = 0
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    
    if x.rank < y.rank:
        x.parent = y

    else:
        y.parent = x
        if x.rank == y.rank:
            x.rank += 1


def make_set(val):
    return Node(val)

def airports(G, k):
    G.sort(key = lambda x: x[2])
    max_vert = 0

    for i in range(len(G)):
        max_vert = max(max_vert, G[i][0], G[i][1])


    V = []

    for i in range(max_vert + 1):
        V.append(make_set(i))

    for i in range(len(G)):
        if G[i][2] >= K:
            break

        union(V[G[i][0]], V[G[i][1]])

    airport_count = 0
    cost = 0

    for i in range(len(G)):
        if G[i][2] >= K:
            break
        
        cost += G[i][2]

    for i in range(max_vert + 1):
        if V[i] == V[i].parent:
            airport_count += 1

    cost += airport_count * k

    return cost, airport_count    

    


graph = [(0, 1, 2), (0, 2, 3), (0, 6, 4), (0, 7, 7), (2, 3, 1), (2, 5, 5), (3, 4, 3),
         (6, 7, 4), (6, 8, 6), (7, 8, 2)]
K = 4
print(airports(graph, K))