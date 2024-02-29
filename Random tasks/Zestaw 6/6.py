def rek(t, i = 0, sumIdx = 0, sumLiczb = 0, ilosc = 0):
    global iloscMin
    global sumaMin

    if i == len(t):
        if sumIdx == sumLiczb and ilosc > 0:
            if ilosc < iloscMin:
                iloscMin = ilosc
                sumaMin = sumLiczb

        return
    
    if sumIdx == sumLiczb and ilosc > 0:
        if ilosc < iloscMin:
            iloscMin = ilosc
            sumaMin = sumLiczb

        return 

    #bierzemy element
    rek(t, i + 1, sumIdx + i, sumLiczb + t[i], ilosc + 1)

    #nie bierzemy elementu
    rek(t, i + 1, sumIdx, sumLiczb, ilosc)



def zad_6(t):
    global iloscMin
    global sumaMin
    iloscMin = 10 ** 10
    sumaMin = 0

    rek(t)

    return sumaMin 

t = [1,7,3,5,11,2]

t2 = [1,0,2,2,2,2,2]

print(zad_6(t))