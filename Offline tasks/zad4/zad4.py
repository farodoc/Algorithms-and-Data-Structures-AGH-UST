#Jakub Konopka
#Na początku przy użyciu BFS'a znajduję najkrótszą sćieżkę z wierzchołka s do t. Jeżeli takowa nie istenieje, zwracam None. Następnie po kolei usuwam krawędzie po których poruszałem się z s do t zaczynając od
#t i t.parent. Przy każdym usunięciu sprawdzam przy użyciu BFS czy długość najkrótszej ścieżki się wydłużyła, czy też może dojście z s do t jest teraz nie możliwe. Jeżeli tak to zwracam tą krawędź.
#Złożoność obliczeniowa: O((V + E) * E)

from zad4testy import runtests
from collections import deque

def BFS(G, s, v1, v2):
    q = deque()
    n = len(G)
    d = [-1 for _ in range(n)]
    d[s] = 0
    visited = [False for _ in range(n)]
    visited[s] = True
    parent = [None for _ in range(n)]
    q.appendleft(s)

    while q:
        u = q.pop()
        for neighbour in G[u]:
            if not visited[neighbour] and ((neighbour != v1 or u != v2) and (neighbour != v2 or u != v1)):
                d[neighbour] = d[u] + 1
                parent[neighbour] = u
                visited[neighbour] = True
                q.appendleft(neighbour)

    return d

def longer( G, s, t ):
    q = deque()
    n = len(G)
    d = [-1 for _ in range(n)]
    d[s] = 0
    visited = [False for _ in range(n)]
    visited[s] = True
    parent = [None for _ in range(n)]
    q.appendleft(s)

    while q:
        u = q.pop()
        for neighbour in G[u]:
            if not visited[neighbour]:
                d[neighbour] = d[u] + 1
                parent[neighbour] = u
                visited[neighbour] = True
                q.appendleft(neighbour)

        if u == t:
            break
                
    if d[t] == -1:
        return None
    
    path_len = d[t]
    v1 = parent[t]
    v2 = t

    for _ in range(path_len):
        res = BFS(G, s, v1, v2)
        if res[t] == -1 or res[t] > d[t]:
            return (v1, v2)
        
        v1, v2 = parent[v1], v1

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )