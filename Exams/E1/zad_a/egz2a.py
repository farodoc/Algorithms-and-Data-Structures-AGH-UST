from egz2atesty import runtests

def coal( A, T ):
    n = len(A)
    magazine = [0] * n
    last_inedx = 0

    for i in range(n):
        for j in range(n):
            if magazine[j] + A[i] <= T:
                magazine[j] += A[i]
                last_inedx = j
                break

    return last_inedx

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )