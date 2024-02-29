def isPrime(x):
    if x == 2 or x == 3:
        return True

    if x % 3 == 0 or x % 2 == 0 or x <= 1:
        return False

    i = 5

    while i <= int(x**0.5):
        if x % i == 0 or x % (i + 2) == 0:
            return False

        i += 6

    return True

def fun(a , r = 0, p = 1):
    if a == 0:
        if isPrime(r) and r > 9:
            print(r)

    else:
        fun(a//10, (a%10) * p + r, p * 10)
        fun(a//10, r, p)

fun(173)