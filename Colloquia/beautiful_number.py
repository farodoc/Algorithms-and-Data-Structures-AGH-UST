# A single digit is one that is exactly once in a given number. A multiple digit is one that is
# more than once in a given number. Natural number A is prettier than the natural number B
# if there are more single digits in A than in B, and if there are the same number of single
# digits, prettier number is one with fewer multiple digits. For example: 123 is prettier than
# 456, 1266 is prettier than 114577 and numbers 2344 and 67333 are equally pretty. We are given
# an array T with natural numbers. Find algorithm pretty_sort(T) that sorts the elements of an
# array T from the prettiest to the least pretty.

from math import log10

def num_types(x):
    t = [0 for _ in range(10)]
    n = int(log10(x)) + 1

    for i in range(n):
        last_digit = x % 10
        x //= 10
        t[last_digit] += 1

    solo = 0
    multi = 0

    for i in range(10):
        if t[i] == 1:
            solo += 1

        elif t[i] > 1:
            multi += 1

    return (solo, multi)

def counting_sort(t, k, type):
    n = len(t)
    B = [0] * n
    C = [0] * k

    for i in range(n):
        C[t[i][type]] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[t[i][type]] - 1] = t[i]
        C[t[i][type]] -= 1

    for i in range(n):
        t[i] = B[i]

def sort_numbers(t):
    n = len(t)
    for i in range(n):
        types = num_types(t[i])
        t[i] = (t[i], types[0], types[1])

    counting_sort(t, 10, 2)
    counting_sort(t, 10, 1)

    for i in range(n//2):
        t[i], t[n - 1 - i] = t[n - 1 - i], t[i]

print(num_types(111))

t = [4412,555555555,123,11,1523]
sort_numbers(t)
print(t)