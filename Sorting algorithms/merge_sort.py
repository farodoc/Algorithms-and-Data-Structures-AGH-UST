import random
def merge_sort(t):
    n = len(t)
    if n > 1:
        mid = n//2
        l = t[:mid]
        r = t[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                t[k] = l[i]
                i += 1

            else:
                t[k] = r[j]
                j += 1

            k += 1

        while i < len(l):
            t[k] = l[i]
            k += 1
            i += 1

        while j < len(r):
            t[k] = r[j]
            k += 1
            j += 1

t = [0]*10
for i in range(10):
    t[i] = random.randint(0,10)

print(t)
merge_sort(t)
print(t)