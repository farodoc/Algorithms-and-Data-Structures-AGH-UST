def czyOk(w, k, wrongW, wrongK):
    if w not in wrongW and k not in wrongK:
        return True
    
    return False

def f(t, i, wrongW, wrongK, suma, aktuSuma = 0):
    global stop

    if stop or i == 4 or aktuSuma > suma:
        return

    if aktuSuma == suma:
        stop = True
        return  

    f(t, i + 1, wrongW, wrongK, suma, aktuSuma)
    
    if czyOk(i // 2, i % 2, wrongW, wrongK):
        wrongW.add(i // 2)
        wrongK.add(i % 2)
        f(t, i + 1, wrongW, wrongK, suma, aktuSuma + t[i])
        


def zad21(t, suma):
    wrongW = set()
    wrongK = set()
    f(t, 0, wrongW, wrongK, suma)
    return stop

stop = False

t = [[1,1,1,1,1,1,1,3],
     [1,2,1,1,1,1,2,1],
     [1,1,3,1,1,1,1,1],
     [1,1,1,4,1,1,1,1],
     [1,1,1,1,5,1,1,1],
     [1,1,1,1,1,6,1,1],
     [1,1,1,1,1,1,7,1],
     [1,1,1,1,1,1,1,8],]


t5 = [1,2,3,4]

t2 = [0 for _ in range(64)]
cnt = 0
for i in range(8):
    for j in range(8):
        t2[cnt] = t[i][j]
        cnt += 1
        

print(zad21(t5,1))


