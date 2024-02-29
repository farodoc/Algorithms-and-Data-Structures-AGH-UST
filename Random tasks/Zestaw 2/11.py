while True: 
    x = int(input("x = "))

    flag = True

    if x < 10:
        print("tak")
        flag = False

    while x > 9:
        lastDigit = x % 10
        x //= 10
        if x % 10 >= lastDigit:
            print("nie")
            flag = False
            break

    if flag:
        print("tak")