def pole(x1, x2, y1, y2):
    return (x2 - x1) * (y2 - y1)

def czyNachodza(x1, x2, y1, y2, X1, X2, Y1, Y2):
    p = False

    if (x1 < X1 < x2 or x1 < X2 < x2) and (y1 < Y1 < y2 or y1 < Y2 < y2):
        p = True

    elif (X1 < x1 < X2 or X1 < x2 < X2) and (Y1 < y1 < Y2 or Y1 < y2 < Y2):
        p = True

    return p

def f(t, i = 0, kwadraty =[], rArea = 2012, cnt = 2):
    if rArea == 0 and cnt == 0:
        return True
    
    if i == len(t) or rArea < 0 or cnt < 0:
        return False

    if i == 0:
        return f(t, i + 1, kwadraty + [(t[i][0], t[i][1], t[i][2], t[i][3])], rArea - pole(t[i][0], t[i][1], t[i][2], t[i][3]), cnt - 1) or f(t, i + 1, kwadraty, rArea, cnt)

    czyOk = True

    for j in range(len(kwadraty)):
        if czyNachodza(t[i][0], t[i][1], t[i][2], t[i][3], t[j][0], t[j][1], t[j][2], t[j][3]):
            czyOk = False
            break

    if czyOk:
        return f(t, i + 1, kwadraty + [(t[i][0], t[i][1], t[i][2], t[i][3])], rArea - pole(t[i][0], t[i][1], t[i][2], t[i][3]), cnt - 1) or f(t, i + 1, kwadraty, rArea, cnt)

    return f(t, i + 1, kwadraty, rArea, cnt)

t = [(0,1006,0,1), (0,1006,5,6)]

print(f(t))