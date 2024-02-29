from math import log10

def leng(liczba):
    if liczba == 0:
        return 0

    return int(log10(liczba)) + 1

def isPrime(x):
    if x == 2 or x == 3:
        return True
    
    if x % 2 == 0 or x % 3 == 0 or x <= 1:
        return False

    i = 5

    while i <= x **0.5:
        if x % i == 0 or x % (i + 2) == 0:
            return False

        i += 6

    return True

def f(x1, x2, dl, res = 0):
    if leng(res) == dl:
        print(res)
        return isPrime(res)

    if x1 == 0 and x2 != 0:
        return f(x1, x2 % (10 ** (leng(x2) - 1)), dl, 10 * res + x2 // (10 **(leng(x2) - 1)))

    if x1 != 0 and x2 == 0:
        return f(x1 % (10 ** (leng(x1) - 1)), x2, dl, 10 * res + x1 // (10 **(leng(x1) - 1)))

    return f(x1 % (10 ** (leng(x1) - 1)), x2, dl, 10 * res + x1 // (10 **(leng(x1) - 1))) + f(x1, x2 % (10 ** (leng(x2) - 1)), dl, 10 * res + x2 // (10 **(leng(x2) - 1)))

a = 31
b = 73

print(f(a, b, leng(a) + leng(b)))