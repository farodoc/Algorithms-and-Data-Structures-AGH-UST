next = True

a,b = 2,2

while next:
    a1 = a
    b1 = b
    while a1 < 2022:
        c = a1 + b1
        if c == 2022:
            next = False
            print("To takie wyrazy: ",a,b)
            break
        a1 = b1
        b1 = c
    
    a += 1
    b += 1


