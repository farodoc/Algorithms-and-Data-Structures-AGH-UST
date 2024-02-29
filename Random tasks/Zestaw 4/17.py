def sumaOtoczenia(t, w, k):
    n = len(t[0])
    sum = 0

    for i,j in (w+1,k),(w+1,k-1),(w,k-1),(w-1,k-1),(w-1,k),(w-1,k+1),(w,k+1),(w+1,k+1):
        if i >= 0 and i < n and j >= 0 and j < n:
             sum += t[i][j]

    return sum

def maxSumaOtoczenia(t):
    n = len(t[0])
    maxSum = 0

    for w in  range(n):
        for k in range(n):
            if sumaOtoczenia(t, w, k) > maxSum:
                maxSum = sumaOtoczenia(t, w, k)
                wiersz = w + 1
                kolumna = k + 1
            
    return (w,k)

t = [[2,2],
     [2,1]]

print(maxSumaOtoczenia(t))