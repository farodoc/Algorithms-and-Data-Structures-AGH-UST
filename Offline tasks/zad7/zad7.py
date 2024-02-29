#Jakub Konopka
#Wartośći pierwszej kolumny wpisuję idąc od góry, ponieważ nie zostaną one nigdy zmienione (można chodzić góra, prawo, dół). Następnie dla każdej kolumny zaczynając od drugiej przechodzę ją na dwa sposoby.
#Najpierw idąc z góry na dół wpisując w odpowiednie miejsce max(max(lewo), góra). Za drugim przejściem idę od dołu do góry wybierając max(max(lewo), dół). Na koniec zwracam maksymalną wartość w komórce n-1, n-1.
#Złożoność obliczeniowa: O(n^2)

from zad7testy import runtests

def maze( L ):
    n = len(L)

    d = [[[-1, -1] for _ in range(n)] for _ in range(n)]

    d[0][0][0] = 0

    i = 1
    while i < n and L[i][0] != '#':
        d[i][0][0], d[i][0][1] = d[i - 1][0][0] + 1, d[i - 1][0][0] + 1
        i += 1 

    for col in range(1, n):
        #idac od gory
        for row in range(n):
            if L[row][col] == '#':
                continue

            if row - 1 >= 0 and d[row - 1][col][0] != -1:
                d[row][col][0] = d[row - 1][col][0] + 1

            #wybieranie maxa z lewej
            if d[row][col - 1][0] > d[row][col - 1][1]:
                maxi_left = d[row][col - 1][0]

            else:
                maxi_left = d[row][col - 1][1]
            ########################

            if maxi_left != -1 and maxi_left + 1 >= d[row][col][0]:
                d[row][col][0] = maxi_left + 1


        #idac od dolu
        for row in range(n - 1, -1, -1):
            if L[row][col] == '#':
                continue

            if row + 1 < n and d[row + 1][col][1] != -1:
                d[row][col][1] = d[row + 1][col][1] + 1

            #wybieranie maxa z lewej
            if d[row][col - 1][0] > d[row][col - 1][1]:
                maxi_left = d[row][col - 1][0]

            else:
                maxi_left = d[row][col - 1][1]
            ########################

            if maxi_left != -1 and maxi_left + 1 >= d[row][col][1]:
                d[row][col][1] = maxi_left + 1


    return max(d[n-1][n-1][0], d[n-1][n-1][1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )