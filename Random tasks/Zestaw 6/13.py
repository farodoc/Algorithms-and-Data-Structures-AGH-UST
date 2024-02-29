def podzial(liczba, j, split):
    if liczba == 0:
        print(split)
        return

    if j == 0:
        last = 1
    
    else:
        last = split[j - 1]

    for i in range(last, liczba + 1):
        split[j] = i
        podzial(liczba - i, j + 1, split)
        split[j] = 0


split = [0,0,0,0] 
podzial(4, 0, split)