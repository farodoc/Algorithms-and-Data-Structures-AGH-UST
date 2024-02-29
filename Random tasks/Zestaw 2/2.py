while True: 
    a = int(input("a = "))
    b = int(input("b = "))
    n = 10 ** int(input("dokladnosc do ilu miejsc:"))

    wynik = int((a * n) / b)
    wynik /= n

    print(wynik)