def findMin(T1, indeksy):
    res = 1000000
    n = len(T1[0])

    for i in range(n):
        if indeksy[i] < n:
            if T1[i][indeksy[i]] < res:
                res = T1[i][indeksy[i]]
                indx = i

    indeksy[indx] += 1

    return res

def przepisz(T1):
    n = len(T1[0])
    T2 = [0 for _ in range(n**2)]

    indeksy = [0 for _ in range(n)]
    miejsceT2 = 0

    for i in range(n**2):
        x = findMin(T1, indeksy)

        T2[miejsceT2] = x
        miejsceT2 += 1

    return(T2)

T1 = [[1,2,3],
      [2,3,4],
      [1,5,5]]

print(przepisz(T1))