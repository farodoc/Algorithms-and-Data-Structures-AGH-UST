def waga(t, i, r, W1 = [], W2 = []):
    global stop

    if stop:
        return False

    if r == 0:
        print(W1, W2)
        stop = True
        return True

    if i == len(t):
        return False

    return waga(t, i + 1, r, W1, W2) or waga(t, i + 1, r - t[i], W1 + [t[i]], W2) or waga(t, i + 1, r + t[i], W1, W2 + [t[i]])


t = [3,2,5,8,12]
stop = False

waga(t, 0, 18)