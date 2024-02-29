for liczba in range(1,1000000):
    suma = 0
    dzielnik = 1
    while dzielnik < int(liczba/2) + 1:
        if liczba % dzielnik == 0:
            suma += dzielnik

        dzielnik += 1
    
    if suma == liczba:
        print(liczba)

print("koniec")