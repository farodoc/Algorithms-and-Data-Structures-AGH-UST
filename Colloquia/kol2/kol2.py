#Jakub Konopka
#Tworzę drzewo MST za pomocą unii z algorytmu Kruskala. Jeżeli mogę zuniować to dodaję do MST wagę tej krawędzi i zwiększam licznik krawędzki. Jeśli jednak nie 
#to oznaczać może to 2 rzeczy. Albo drzewo MST zostasło utworzone i sprawdzam czy liczba krawędzi wynisi V - 1 i zwracam wtedy sumę wag krawędzi MST. W przeciwnym razie
#drzewo jeszcze nie powstało a musielibyśmy pominąć krawędz(krawędzie są posortowane wagowo), krawędź pominięta byłaby wieksza od obecnych lecz mniejsza od tych, 
#których jeszcze brakuje. Stąd nie da się tymi krawędziami swtorzyć beauty tree. Przerywam wieć działanie algorytmu Kruskala i usuwam więc pierwszą krawędź ze zbioru 
#edges i uruchamiam algorytm ponownie.
#Złożoność obliczeniowa: O(VElog*E)

from kol2testy import runtests
from math import inf

class Node:
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.rank = 0


def find(x):
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


def kruskal(G, n):
    MST = []
    edge_cnt = 0

    V = [Node(i) for i in range(n)]

    for edge in G:
        u, v, weight = edge
        if union(V[u], V[v]):
            MST.append(weight)
            edge_cnt += 1

        else:
            if edge_cnt < n - 1:
                return -inf
            
            else:
                res = 0
                for cost in MST:
                    res += cost

                return res

    return None


def beautree(G):
    n = len(G)
    edges = []

    for u in range(n):
        for v, weight in G[u]:
            if [v, u, weight] not in edges:
                edges.append([u, v, weight])


    edges.sort(key=lambda x: x[2])
    E = len(edges)

    for _ in range(E - n + 1): #tyle maksymalnie mogę usunąć krawędzi aby stworzenie MST było nadal możliwe
        temp_res = kruskal(edges, n)
        if temp_res != -inf:
            return temp_res
        
        edges.remove(edges[0])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )