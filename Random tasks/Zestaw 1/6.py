p = 1
q = 10
eps = 0.0001

while q - p > eps:
    srednia = (p + q) / 2
    if srednia ** srednia > 2022:
        q = srednia
    else:
        p = srednia

print((p + q) / 2)