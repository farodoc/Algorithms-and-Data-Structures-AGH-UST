pierwiastek = 0.5 ** 0.5
ostatniWyraz = 0.5 ** 0.5

for i in range(100):
    ostatniWyraz = (0.5 + 0.5 * ostatniWyraz) ** 0.5
    pierwiastek *= ostatniWyraz
    pi = 2/pierwiastek
    print(pi)