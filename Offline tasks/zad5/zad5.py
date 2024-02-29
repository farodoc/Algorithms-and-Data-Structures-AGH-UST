#Jakub Konopka
#Czarną dziurę traktuję jako nowy wierzchołek. Na początku dane przekształcam na listę sąsiedztwa z listy E. Następnie z listy S dodaję krawędzie miedzy nowym wierzchołkiem (czarną dziurą), a wierzchołkami,
#które obok niej się znajdowały. Dla tak przygotowanych danych używam Dijkstry i zwracam odpowiedni wynik.
#Złożoność obliczeniowa: przerobienie danych O(E + S), reszta algorytmu O(ElogV)


from zad5testy import runtests
from queue import PriorityQueue
from math import inf

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n + 1)]
    q = PriorityQueue()
    d = [inf] * (n + 1)
    visited = [False] * (n + 1)

    d[a] = 0

    for i in range(len(E)):
        G[E[i][0]].append((E[i][2],E[i][1]))
        G[E[i][1]].append((E[i][2],E[i][0]))

    for i in range(len(S)):
        G[n].append((0, S[i]))
        G[S[i]].append((0, n))

    q.put((0, a))
    
    def relax(u, v):
        if d[v[1]] > d[u[1]] + v[0]:
            d[v[1]] = d[u[1]] + v[0]
    
    while not visited[b] and not q.empty():
        u = q.get()

        if visited[u[1]]:
            continue

        for v in G[u[1]]:
            if not visited[v[1]]:
                relax(u, v)
                q.put((d[v[1]], v[1]))

        visited[u[1]] = True

    if d[b] == inf:
        return None
    
    return d[b]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )