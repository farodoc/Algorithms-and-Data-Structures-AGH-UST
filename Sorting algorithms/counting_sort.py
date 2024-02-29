import random

def counting_sort(t, k):
    n = len(t)
    B = [0] * n
    C = [0] * (k + 1)

    for i in range(n):
        C[t[i]] += 1

    for i in range(1, k + 1):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[t[i]] - 1] = t[i]
        C[t[i]] -= 1

    for i in range(n):
        t[i] = B[i]


t = [0]*10
for i in range(10):
    t[i] = random.randint(0,10)

print(t)
counting_sort(t, 10)
print(t)