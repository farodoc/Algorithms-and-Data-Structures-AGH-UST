while True:    
    n = int(input("przedzial od 1 do "))
    licznik = 0

    a = 1
    while a <= n:
        b = a
        while b <= n:
            c = b
            while c <= n:
                licznik += 1
                c *= 5

            b *= 3
        
        a *= 2


    print(licznik)