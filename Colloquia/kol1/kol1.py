#Jakub Konopka
#Dla każdego zi tworze kopie tablicy, wywoluje na niej quickSelect na odpowiednim przedziale w celu znaleznienia tego elementu, i dodaje go do sumy. Na koniec 
#zwracam sume.
#Złożoność obliczeniowa: O(np)

from kol1testy import runtests

def partition(t, left, right):
    x = t[right]
    i = left

    for j in range(left, right):
        if t[j] <= x:
            t[i], t[j] = t[j], t[i]
            i += 1

    t[i], t[right] = t[right], t[i]
    return i

def quick_select(t, left, right, k):
    q = partition(t, left, right)

    while q != k:
        if q < k:
            q = partition(t, q + 1, right)
        
        else:
            q = partition(t, left, q - 1)


    return t[q]

def ksum(T, k, p):
    n = len(T)
    sum = 0

    for i in range(n - p + 1):
        arr = T[i:i+p]
        sum += quick_select(arr, 0, p - 1, p - k)
    
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )