#Jakub Konopka
#W algorytmie rozmnazam tablice odleglosci. Ma ona V elementow [x,y], gdzie x oznacza minimalny koszt dojscia do tego wierzcholka
#bez rabowania zadnego zamku do tej pory, a y przeciwnie. Algorytm to zmodyfikowany dijkstra, do kolejki priorytetowej wrzucam
#koszt dojscia, wierzcholek i wartość true/false w zależności od tego czy obrabowaliśmy zamek. Na koniec zwracam wartość minimalną
#z kosztów dojścia do wierzchołka t (nie koniecznie musieliśmy rabować zamek).
#Złożoność obliczeniowa to ElogV (algorytm dijkstry), E w pesymistycznym przypadku to V^2 => złożoność to V^2logV

from egz1Atesty import runtests
from math import inf
from queue import PriorityQueue

def gold(G,V,s,t,r):
  n = len(G)

  d = [[inf, inf] for _ in range(n)]
  d[s][0] = 0
  d[s][1] = -V[s]
  #0 - bez rabunku
  #1 - z rabunkiem
  q = PriorityQueue()
  #obrabowany pierwszy zamek czy nie
  q.put((0, (s, False)))
  q.put((-V[s], (s, True)))

  def relax(u, v, cost, robbed):
    if not robbed:
      if d[u][0] + cost < d[v][0]:
        d[v][0] = d[u][0] + cost
        q.put((d[v][0], (v, False)))

      if d[u][0] + cost - V[v] < d[v][1]:
        d[v][1] = d[u][0] + cost - V[v]
        q.put((d[v][1], (v, True)))

    else:
      if d[u][1] + 2 * cost + r < d[v][1]:
        d[v][1] = d[u][1] + 2 * cost + r
        q.put((d[v][1], (v, True)))


  while not q.empty():
    dist, krotka = q.get()
    u, robbed = krotka
    
    for v, cost in G[u]:
      relax(u, v, cost, robbed)


  return min(d[t])
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )