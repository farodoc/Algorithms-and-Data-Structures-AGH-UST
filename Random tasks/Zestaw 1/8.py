def isPrime(liczba):
    if liczba < 2:
        return False

    for i in range(2,int(liczba**0.5) + 1):
        if liczba%i == 0:
            return False

    return True

print(isPrime(13))