from egz2atesty import runtests

def is_stronger(p1, p2):
  return p1[0] > p2[0] and p1[1] > p2[1]

def dominance(P):
  n = len(P)
  max_strong = 0

  for i in range(n):
    curr_strong = 0
    for j in range(n):
      if is_stronger(P[i], P[j]):
        curr_strong += 1

    max_strong = max(max_strong, curr_strong)

  return max_strong


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = False )