def cztZlozona(x):
    if x == 2 or x == 3:
        return False

    for i in range(2, int(x ** 0.5) + 2):
        if x % i == 0:
            return True
    
    return False

def f(A, B, res = 0, multi = 1, braneA = False):
    if A == 0 and B == 0:
        if braneA:
            return cztZlozona(res)
        
        return 0

    if A == 0:
        return 0

    if B == 0:
        return f(A - 1, B, res + multi, multi * 2, True)

    return f(A - 1, B, res + multi, multi * 2, True) + f(A, B - 1, res, multi * 2, False)

print(f(2,3))

    
