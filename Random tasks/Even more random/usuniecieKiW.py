def ile1(liczba):
    cnt = 0
    while liczba > 0:
        if liczba % 2 == 1:
            cnt += 1

        liczba //= 2

    return cnt

def remove(t):
    dl = len(t[0])

    for w in range(dl):
        for k in range(dl):
            t[w][k] = ile1(t[w][k])

    
        
    for w in range(dl):
        for k1 in range(dl - 1):
            for k2 in range(k1 + 1, dl):
                nieparzyste1 = True
                for i in range(dl):
                    for j in range(dl):
                        if i != w and j != k1 and j != k2:
                            if t[i][j] % 2 == 0:
                                nieparzyste1 = False
                                break

                    if not nieparzyste1:
                        break
                
                if nieparzyste1:
                    return True
    
    return False


t = [[1,1,1,1],
     [1,1,3,1],
     [1,3,3,1],
     [1,1,1,3]]

print(remove(t))
