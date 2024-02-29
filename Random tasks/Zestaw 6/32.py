def f(t, k, i = 0, s1 = 0, m1 = 0, s2 = 0, m2 = 0):
    if s1 == s2 and m1 + m2 == k:
        return True

    if i == len(t):
        return False

    return f(t, k, i + 1, s1, m1, s2, m2) or f(t, k, i + 1, s1 + t[i], m1 + 1, s2, m2) or f(t, k, i + 1, s1, m1, s2 + t[i], m2 + 1)


t = [1,2,4,7,5,2,3]
print(f(t,10))