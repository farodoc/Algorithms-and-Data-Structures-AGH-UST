def bin_search(T, x):
    left = 0
    right = len(T) - 1

    while left < right:
        mid = (left + right)//2
        if T[mid] == x:
            return mid
        
        if T[mid] > x:
            right = mid
        
        else:
            left = mid + 1

    return left

def LIS(T):
    n = len(T)
    arr = []
    arr.append(T[0])

    for i in range(1, n):
        if arr[len(arr) - 1] < T[i]:
            arr.append(T[i])

        else:
            idx = bin_search(arr, T[i])
            arr[idx] = T[i]

    return arr

T = [2,3,1,2,5,3,7]
print(LIS(T))