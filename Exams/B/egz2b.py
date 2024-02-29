#Norbert Dziwak
#T(i,j) - minimalna suma odległości biorąc pod uwagę wierzowce włącznie do i-tego oraz parkingi włącznie do j-tego (i-ty wierzowiec nie musi mieć j-tego parkingu),
#w algorytmie na początku wypełniam pierwszą kolumnę(pierwszy wierzowiec) najmniejszymi potencjalnie wartościami. Dla każdej kolejnej kolumny są 2 przypadki.
#T(i,j) = min(T(i, j-1), T(i-1,j-1) + odl(i-ty-wierzowiec, j-ty-parking)), dla 1 <= i <= n, i <= j <= m
#Albo dla i-tego wierzowca bierzemy j-ty parking i wtedy patrzymy jak najlepiej dobrać parkingi dla i-1 wierzowców gdy mamy do dyspozycji j-1 (T(i-1,j-1)) parkingów lub 
#drugi przypadek, że nie korzystamy z j-tego parkingu (dziedziczymy z góry).
#Złożoność: O(nm)

from egz2btesty import runtests
from math import inf

def parking(X,Y):
  n = len(X)
  m = len(Y)

  def leng(x, y):
    return abs(X[x] - Y[y])

  T = [[inf for _ in range(n)] for _ in range(m)]
  T[0][0] = leng(0, 0)

  for i in range(1, m):
    T[i][0] = min(T[i - 1][0], leng(0, i))


  for x in range(1, n):
    for y in range(x, m):
      T[y][x] = min(T[y - 1][x], T[y - 1][x - 1] + leng(x, y))

  return T[m - 1][n - 1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )