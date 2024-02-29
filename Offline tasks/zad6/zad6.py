#Jakub Konopka
#Na początku dla każdego pracownika wybieram dowolną wolną maszynę. Tych których opcje były już zajęte, dodaję do tablicy unmatched. Następnie dla każdego pracownika z tablicy unmatched uruchamiam algorytm, który
#dla wszystkich maszyn na których mógłby pracować sprawdza, czy aktualnych umieszczonych tam pracowników nie da się umieścić gdzie indziej. Jeżeli się da to go przepina i maszyna jest już wolna dla naszego pracownika.
#Jeżeli jednak u drugiego badanego pracownika też nie da się znaleźć maszyny to algorytm uruchamia się ponownie dla aktualnego pracownika. Jeżeli na jakimś etapie uda się przepiąć pracownika, 
#to funkcja zwróci True i wszystkich poprzednich pracowników przepinamy na maszyny swoich następców. Jeśli jednak nie uda się tego dokonać to algorytm się dla tego pracownika zakończy bez żadnych zmian.
#Złożoność obliczeniowa: O(E*sqrt(V))

from zad6testy import runtests

def binworker(M):
    n = len(M)
    unmatched = []
    selected = [-1 for _ in range(n)]

    for worker in range(n):
        notFound = True
        for machine in M[worker]:
            if selected[machine] == -1:
                selected[machine] = worker
                notFound = False
                break

        if notFound:
            unmatched.append(worker)

    
    def DFS(worker):
        for machine in M[worker]:
            if not visited[machine]:
                visited[machine] = True

                if selected[machine] == -1 or DFS(selected[machine]):
                    selected[machine] = worker
                    return True
            
        return False
    
    for worker in unmatched:
        visited = [False] * n
        DFS(worker)

    
    cnt = 0

    for i in range(n):
        if selected[i] != -1:
            cnt += 1

    return cnt


#runtests( binworker, all_tests = True )

T = [(2, 3), (0, 1, 3), (0, 2), (1, 3, 4), (2, 3)]
print(binworker(T))