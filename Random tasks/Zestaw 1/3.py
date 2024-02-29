while True:
    podanaSuma = int(input("Podaj sume: "))

    fib = [1,1]
    notExist = True

    while fib[len(fib) - 1] < podanaSuma:
        fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])

    for i in range(0,len(fib) - 1):
        suma = 0 
        p = i

        while suma < podanaSuma:
            suma += fib[p]
            p += 1 

        if suma == podanaSuma:
            print("istnieje taki podciag")
            notExist = False
            break

    if notExist:
        print("nie istnieje taki podciag")