def f(x):
    return 1/x

while True: 
    k = int(input("przedzial od 1 do "))
    eps = 0.1
    x1 = 1
    x2 = x1 + eps
    pole = 0

    while x2 < k:
        pole += f((x1 + x2) / 2) * eps
        x1 += eps
        x2 += eps

    print(pole)

