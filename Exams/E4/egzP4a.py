from egzP4atesty import runtests 

def bin_search(num, T):
    left = 0
    right = len(T) - 1

    while left != right:
        mid = (left + right)//2
        if T[mid] == num:
            return mid
        
        if T[mid] > num:
            right = mid

        else:
            left = mid + 1

    return right


def LIS(T):
    n = len(T)
    res = [T[0]]

    for i in range(1, n):
        m = len(res)
        if res[m - 1] <= T[i]:
            res.append(T[i])

        else:
            idx = bin_search(T[i], res)
            res[idx] = T[i]

    return len(res)

def mosty (T):
    T.sort(key = lambda x:(x[0], x[1]))
    n = len(T)
    T2 = [T[i][1] for i in range(n)]

    return LIS(T2)

runtests ( mosty, all_tests=False )