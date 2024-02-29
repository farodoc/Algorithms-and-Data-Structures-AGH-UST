def partition(arr, left, right):
    x = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_select(arr, left, right, k):
    q = partition(arr, left, right)
    while q != k:
        if q > k:
            q = partition(arr, left, q - 1)

        else:
            q = partition(arr, q + 1, right)

    

def section(T, p, q):
    n = len(T)
    quick_select(T ,0, n - 1, p)
    quick_select(T, p, n - 1, q)
    print(T[p:q+1])

t = [123,23,112,75,2,198,156,143]
section(t, len(t)-1, len(t)-1)