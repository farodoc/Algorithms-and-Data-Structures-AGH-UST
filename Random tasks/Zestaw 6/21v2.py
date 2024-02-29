def suma(T, sum, cols, w=0):
    if sum == 0:
        return True

    if sum < 0 or w == len(T):
        return False
    
    for i in range(len(T)):
        if cols[i] == False:
            cols[i] = True
            if suma(T, sum - T[w][i], cols, w + 1):
                return True
            else:
                cols[i] = False

    if suma(T, sum, cols, w + 1):
        return True

    else:
        return False
        
def K(T, sum):
    cols = [False for _ in range(len(T))]
    return suma(T, sum, cols)

t = [[1,1,1,1,1,1,1,3],
     [1,2,1,1,1,1,2,1],
     [1,1,3,1,1,1,1,1],
     [1,1,1,4,1,1,1,1],
     [1,1,1,1,5,1,1,1],
     [1,1,1,1,1,6,1,1],
     [1,1,1,1,1,1,7,1],
     [1,1,1,1,1,1,1,8],]

print(K(t,36))