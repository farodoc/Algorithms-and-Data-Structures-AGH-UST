import random

def heapify(t, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    max_idx = i

    if l < n and t[l] > t[max_idx]:
        max_idx = l

    if r < n and t[r] > t[max_idx]:
        max_idx = r

    if max_idx != i:
        t[i], t[max_idx] = t[max_idx], t[i]
        heapify(t, max_idx, n)


def heap_sort(t):
    n = len(t)

    for i in range((n-2)//2, -1, -1):
        heapify(t, i, n)

    for i in range(n - 1, -1 ,-1):
        t[0], t[i] = t[i], t[0]
        heapify(t, 0, i)




t = [0]*10
for i in range(10):
    t[i] = random.randint(0,10)

print(t)
heap_sort(t)
print(t)