#Jakub Konopka
#W algorytmie najpierw przedstawiam wszystkie slowa według jednej zasady, zawężając się w słowie od lewej i od prawej strony na raz, gdy napotkam litere mniejszą to odwracam słowo, w przypadku gdy wyraz jest od razu
#dobrze ustawiony nic z nim nie robię. Następnie sortuję całą tablicę i wyszukuję najdłuższego podciągu składającego się z takich samych słów.
#Złożoność obliczeniowa: O(N + nlogn)

from zad3testy import runtests

def merge_sort(t):
    n = len(t)
    
    if n > 1:
        mid = n//2
        leftArr = t[:mid]
        rightArr = t[mid:]

        merge_sort(leftArr)
        merge_sort(rightArr)

        i = 0
        j = 0
        k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                t[k] = leftArr[i]
                i += 1
            
            else:
                t[k] = rightArr[j]
                j += 1
            
            k += 1

        while i < len(leftArr):
            t[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            t[k] = rightArr[j]
            j += 1
            k += 1


def strong_string(T):
    n = len(T)
    
    for i in range(n):
        swap = False
        word = T[i]
        for j in range(len(T[i])//2):
            if word[j] > word[len(word) - j - 1]:
                swap = True
                break
            
            elif word[j] < word[len(word) - j - 1]:
                break

        if swap:
            T[i] = word[::-1]
                

    merge_sort(T)

    strongest = 0
    i = 0

    while i < n - 1:
        if T[i] == T[i + 1]:
            word = T[i]
            currCnt = 2
            i += 2
            while i < n and T[i] == word:
                currCnt += 1
                i += 1
            
            if currCnt > strongest:
                strongest = currCnt

        else:
            i += 1

    return strongest


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )