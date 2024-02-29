#czy graf dwudzielny
def dwudzielny(G):
    colors = (-1)*len(G)
    Q = Queue()
    start.v
    Q.pyt(start.v)
    colors[start.v] = 1
    while not Q.empty():
        v = Q.get()
        for v in G[v]:
            if colors[v] == -1:
                colors[v] = (colors[v] + 1) % 2
                Q.put(v)
            
            else:


#dany jest graf G, jako macierz sasoedztwa. Czy istnieje cykl dlugosci 4
def zad3(G):
    n = len(G)
    for i in range(n):
        for j in range(i + 1, n):
            cnt = 0
            for k in range(n):
                if G[i][k] and G[j][k]:
                    cnt += 1

            if cnt >= 2:
                return True
            
    return False