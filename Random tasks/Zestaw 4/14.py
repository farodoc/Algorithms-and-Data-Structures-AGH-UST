def ile1wbin(liczba):
    cnt = 0
    while liczba > 0:
        cnt += liczba % 2
        liczba //= 2

    return cnt

def pokrytyObszar(t1, t2, w, k):
    n = len(t1[0])
    cnt = 0

    for i in range(n):
        for j in range(n):
            if t1[i][j] == t2[i + w][j + k]:
                cnt += 1

    if cnt/n**2 > 0.33:
        return True

    return False

def pokrycie(t1, t2):
    n1 = len(t1[0])
    n2 = len(t2[0])

    T1jedynki = [[0 for _ in range(n1)] for _ in range(n1)]
    T2jedynki = [[0 for _ in range(n2)] for _ in range(n2)]

    for i in range(n1):
        for j in range(n1):
            T1jedynki[i][j] = ile1wbin(t1[i][j])

    for i in range(n2):
        for j in range(n2):
            T2jedynki[i][j] = ile1wbin(t2[i][j])

    for i in range(n2 - n1 + 1):
        for j in range(n2 - n1 + 1):
            if pokrytyObszar(T1jedynki, T2jedynki, i, j):
                return True
        
    return False

t1 = [[1,1],
      [2,4]]

t2 = [[3,7,12],
      [1,3,1],
      [3,3,3]]

print(pokrycie(t1, t2))
    
