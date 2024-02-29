#Jakub Konopka
#Program działa niczym heapsort, lecz podczas zamiany elementów (ostatniego i roota) sprawdza czy ten aktualnie największy element po odjęciu wartości vaporized (jaka jest zasymulowaną wartością roztopionego
#śniegu inkremenrującą się o 1 każdego dnia) jest dodatni (czy znajduje się tam jakikolwiek śnieg). Jeżeli tak, to dodaję go do finalnego wyniku, oczywiście pomniejszonego o wartość vaporized.
#Operacje te są przeprowadzane do momentu aż na badanej kupce nie będzie znajdował się śnieg lub został on zebrany już ze wszystkich kupek. Ostatecznie program zwraca wartość res, w której przechowywana jest
#objętość zebranego śniegu.
#Algorytm ten działa, gdyż wybiera on opłacalne kupki do zabrania. Nie jest ważna kolejność ich ostatecznego zbioru, ważne jest, które kupki będziemy chcieli zebrać. Pętla for w pewnym sensie symuluje liczbe dni
#przez jakie będziemy zbierać śnieg i dla tych dni wybiera największe kupki. 
#W przypadku gdy nie można wywieźć wszystkich kupek, niektóre muszą zostać pominięte. Stąd dana kupka śniegu może zostać ostatecznie wzięta lub nie. Jeżeli nie została wzięta pod uwagę przez algorytm, 
#to oznacza to, że śnieg był zbierany przez liczbe dni większą niż początkowa liczba m^3 śniegu na tej kupce. Wynika z tego, że jeśli w jakikolwiek dzień wybralibyśmy tą kupkę, wartość jaką przygarneliśmy 
#jest mniejsza od liczby dni przez jakie będziemy jeszcze wywoźić śnieg. Więc ponieważ nie wzięliśmy optymalnej kupki to do końca okresu wywozu tracimy dziennie 1 m^3 śniegu więcej niż gdybyśmy wzięli optymalna 
#kupkę (ponieważ nigdy nie wzięlibyśmy tej nieoptymalnej kupki), a ponieważ liczba dni jest większa od objętości tej nieoptymalnej kupki śniegu to w ostatecznym rozrachunku stracilibyśmy >= 1 m^3 na tej operacji.
#Złożoność obliczeniowa: O(nlogn)

from zad2testy import runtests

def heapify(t, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    max_idx = i

    if l < n and t[l] > t[max_idx]:
        max_idx = l
    
    if r < n and t[r] > t[max_idx]:
        max_idx = r

    if max_idx != i:
        t[i], t[max_idx] = t[max_idx], t[i]
        heapify(t, max_idx, n)

def snow( S ):
    n = len(S)
    vaporized = 0
    res = 0

    for i in range((n - 2) // 2, -1, -1):
        heapify(S, i, n)

    for i in range(n - 1, -1, - 1):
        S[0], S[i] = S[i], S[0]

        if S[i] - vaporized > 0:
            res += S[i] - vaporized
            vaporized += 1
            heapify(S, 0, i)

        else:
            break

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( snow, all_tests = True )