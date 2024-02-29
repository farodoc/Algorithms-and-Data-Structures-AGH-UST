def numOf1(x):
    cnt = 0

    while x > 0:
        if x % 2 == 1:
            cnt += 1

        x //= 2

    return cnt

def f(t, i = 0, s1 = 0, s2 = 0, s3 = 0):
    if i == len(t):
        return s1 == s2 and s2 == s3

    return f(t, i + 1, s1 + numOf1(t[i]), s2, s3) or f(t, i + 1, s1, s2 + numOf1(t[i]), s3) or f(t, i + 1, s1, s2, s3 + numOf1(t[i]))

t = [5,7,15]
print(f(t))