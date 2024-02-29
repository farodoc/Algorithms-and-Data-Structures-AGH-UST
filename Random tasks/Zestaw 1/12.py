while True: 
    liczba1 = int(input("Liczba a:"))
    liczba2 = int(input("Liczba b:"))
    liczba3 = int(input("Liczba c:"))

    if liczba1 <= liczba2 and liczba1 <= liczba3:
        najmniejsza = liczba1
    elif liczba2 <= liczba1 and liczba2 <= liczba3:
        najmniejsza = liczba2
    else:
        najmniejsza = liczba3

    najwieksyDzielnik = 1

    for i in range(2,najmniejsza + 1):
        if liczba1 % i == 0 and liczba2 % i == 0 and liczba3 % i == 0:
            najwieksyDzielnik = i

    print(najwieksyDzielnik)