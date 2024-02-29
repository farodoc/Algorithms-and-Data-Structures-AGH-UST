def merge_sort(t):
    n = len(t)
    if n > 1:
        mid = n//2
        left = t[:mid]
        right = t[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                t[k] = left[i]
                i += 1

            else:
                t[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            t[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            t[k] = right[j]
            j += 1
            k += 1

def chaos_index(t):
    n = len(t)

    for i in range(n):
        t[i] = (t[i], i)

    merge_sort(t)

    maxi = 0

    for i in range(n):
        if abs(i - t[i][1]) > maxi:
            maxi = abs(i - t[i][1])

    return maxi

t = [0, 2, 1.1, 2]
print(chaos_index(t))