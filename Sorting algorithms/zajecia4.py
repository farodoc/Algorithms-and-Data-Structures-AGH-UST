from math import log10

#posortowac tablice n liczb z zakresu <0, n^2 - 1>

def counting(A, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for i in range(n):
        C[A[i]] += 1
    
    for i in range(n - 1, -1, -1):
        B[C[A[i]]] = A[i]
        C[A[i]] -= 1
    
    for i in range(n):
        A[i] = B[i]


def radix(t):
    n = len(t)

#tablica A o dlugosci n. Elementy naleza do B. |B| = logn

def map_numbers(t):
    n = len(t)
    arr = []
    for i in range(n):
        test = True
        for j in range(len(arr)):
            if arr[j] == t[i]:
                t[i] = j
                test = False
                break
                
        if test:
            arr.append(t[i])
            t[i] = len(arr) - 1
