a0 = 0
a1 = 1
b0 = 2
b1 = 2
i = 0

while True:
    x = int(input("x = "))
    if x == a0:
        print("b" + str(i) + " = " + str(b0))
        i += 1
        a0, a1, b0, b1 = a1, a1 - b1 * a0, b1, b1 + 2 * a1 
    
    else:
        print("koniec")
        break
