def waga(t, szukanaWaga, aktuWaga = 0, i = 0):
    if szukanaWaga == aktuWaga:
        return True

    if i == len(t):
        if szukanaWaga == aktuWaga:
            return True
        
        return False

    return waga(t, szukanaWaga, aktuWaga + t[i], i + 1) or waga(t, szukanaWaga, aktuWaga, i + 1) or waga(t, szukanaWaga + t[i], aktuWaga, i + 1)


t = [3,2,5,8,12]

print(waga(t, 4))