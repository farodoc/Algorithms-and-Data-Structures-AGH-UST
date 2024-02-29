import random

def bucket_sort(t):
    n = len(t)
    buckets = [[] for _ in range(n)]

    for i in range(n):
        buckets[t[i]].append(t[i])

    for i in range(n):
        buckets[i].sort()

    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            t[k] = buckets[i][j]
            k += 1


t = [0]*10
for i in range(10):
    t[i] = random.randint(0,9)

print(t)
bucket_sort(t)
print(t)