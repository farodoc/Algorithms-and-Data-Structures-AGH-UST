from egz3atesty import runtests

def snow( T, I ):
    n = len(I)

    I.sort(key = lambda x:x[0])

    F = [1] * n

    for i in range(1, n):
        for j in range(i):
            if I[j][1] >= I[i][0]:
                F[i] += 1

    return max(F)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )