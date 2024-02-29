from math import log
import random

def merge_sort(t):
    n = len(t)
    if n > 1:
        mid = n//2
        left = t[:mid]
        right = t[mid:]

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                t[k] = left[i]
                i+= 1

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


def fast_sort(t, a):
    n = len(t)
    arr = [[] for _ in range(n)]

    for i in range(n):
        bucket_idx = int(log(t[i], a) * n)
        arr[bucket_idx].append(t[i])
    
    for i in range(n):
        merge_sort(arr[i])

    k = 0
    for i in range(n):
        for j in range(len(arr[i])):
            t[k] = arr[i][j]
            k += 1

n = 20
t = [0]*n
a = 5

for i in range(n):
    power = random.random()
    t[i] = a ** power

print(t)
fast_sort(t,5)
print(t)