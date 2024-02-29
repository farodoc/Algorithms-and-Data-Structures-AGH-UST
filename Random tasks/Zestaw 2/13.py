while True:
    x = int(input("x = "))
    flag = True
    unikat = x % 10

    if x < 11:
        print("tak")
        flag = False

    else:
        while x > 0:
            x //= 10
            if unikat == x % 10:
                print("nie")
                flag = False
                break
    
    if flag:
        print("tak")