def szachy(t, w, k):
    if w == 7:
        return t[w][k]

    if k > 0:
        left = szachy(t, w + 1, k - 1)
    
    else:
        left = float('inf')

    if k < 7:
        right = szachy(t, w + 1, k + 1)

    else:
        right = float('inf')

    middle = szachy(t, w + 1, k)

    return min(left, middle, right) + t[w][k]

t = [[1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1],
     [2,2,2,2,2,2,2,3]]

print(szachy(t, 0, 0))