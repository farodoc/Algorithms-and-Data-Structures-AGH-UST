import math

while True:
    x = int(input("x = "))
    liczbaCyfr = int(math.log(x,10)) + 1

    flag = True

    while x > 0:
        if x % 10 == liczbaCyfr:
            print("tak, ", liczbaCyfr)
            flag = False
            break
        x //= 10

    if flag:
        print("nie, ", liczbaCyfr)