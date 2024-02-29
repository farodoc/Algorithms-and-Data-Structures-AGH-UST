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
    left = 0
    right = len(t) - 1
    q = partition(t, left, right)

    while q != k:
        if q > k:
            q = partition(t, left, q - 1)

        else:
            q = partition(t, q + 1, right)


def median(t):
    n = len(t)
    start_diagonal = (n**2 - n)//2
    end_diagonal = (n**2 + n)//2
    arr = [0]*(n**2)
    k = 0
    for i in range(n):
        for j in range(n):
            arr[k] = t[i][j]
            k += 1

    quick_select(arr, 0, n**2 - 1, start_diagonal)
    quick_select(arr, start_diagonal, n**2 - 1, end_diagonal)
    idx = start_diagonal
    print(arr)
    for i in range(n):
        t[i][i] = arr[idx]
        idx += 1

    idx = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            t[j][i] = arr[idx]
            idx += 1

    idx = end_diagonal
    for i in range(n - 1):
        for j in range(i + 1, n):
            t[i][j] = arr[idx]
            idx += 1

T = [[2,3,5],[7,11,13],[17,19,23]]
median(T)
print(T[0])
print(T[1])
print(T[2])