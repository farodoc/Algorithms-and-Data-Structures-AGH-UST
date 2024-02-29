#Jakub Konopka
#Na początku zbieram wszystkie rozlane plany do kupy (na osi po której się przemieszczamy). Następnie przechodzę jednorazowo po pierwszym wierszu, za każdą iteracją odejmując po jednym litrze paliwa z baku
#i sprawdzając czy znajdujemy się na plamie. Jeśli jesteśmy na plamie to dodaję jej pojemność do kolejki priorytetowej. Jeśli przy którejś iteracji zabraknie paliwa (fuel == 0), to znaczy, że kiedyś musieliśmy 
#zatankować więc zwiększam licznik przystanków o 1 i zwiekszam aktualne paliwo o największe do tej pory umieszczone w kolejce.
#Złożoność obliczeniowa: O(nm)

from zad8testy import runtests
from collections import deque
from queue import PriorityQueue
from math import inf


def plan(T):
    n = len(T[0])
    m = len(T)
    road = [0] * n
    visited = [[False for _ in range(n)] for _ in range(m)]

    for i in range(n):
        if visited[0][i] or T[0][i] == 0:
            continue
        
        fuel = 0
        q = deque()
        q.append((0,i))
        visited[0][i] = True

        while q:
            w, k = q.popleft()
            fuel += T[w][k]
            move = [(w-1,k),(w,k+1),(w+1,k),(w,k-1)]

            for W, K in move:
                if (0 <= W < m) and (0 <= K < n) and not visited[W][K] and T[W][K] != 0:
                    visited[W][K] = True
                    q.append((W,K))

        road[i] = fuel


    cnt = 0
    fuel = 0
    Q = PriorityQueue()

    for i in range(n - 1):
        if road[i] != 0:
            Q.put((-road[i], road[i]))

        if fuel == 0:
            cnt += 1
            _, additional_fuel = Q.get()
            fuel = additional_fuel

        fuel -= 1

    return cnt

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )