import random

def partition(t, left, right):
    x = t[right]
    i = left

    for j in range(left, right):
        if t[j] <= x:
            t[i], t[j] = t[j], t[i]
            i += 1

    t[i], t[right] = t[right], t[i]
    return i

def quick_select(t, k):
    left = 0
    right = len(t) - 1
    q = partition(t, left, right)

    while q != k:
        if q > k:
            q = partition(t, left, q - 1)

        else:
            q = partition(t, q + 1, right)

    return t[k]

t = [0]*10
for i in range(10):
    t[i] = random.randint(0,10)

print(t)
print(quick_select(t, 0))