def merge_sort(t):
    n = len(t)
    if n > 1:
        mid = n//2
        leftArr = t[:mid]
        rightArr = t[mid:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i = 0
        j = 0
        k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                t[k] = leftArr[i]
                i += 1

            else:
                t[k] = rightArr[j]
                j += 1

            k += 1

        while i < len(leftArr):
            t[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            t[k] = rightArr[j]
            j += 1
            k += 1



def sort_square(t):
    n = len(t)
    arr = [0] * n
    for i in range(n):
        for j in range(n):
            arr[j] = t[j][i]
        
        merge_sort(arr)

        for j in range(n):
            t[j][i] = arr[n - j - 1]

t = [[2,3,5],[7,11,13],[17,19,23]]
sort_square(t)
print(t)