n = 10
t1 = [2,1,18,3,7,1,4,2,1,7]
t2 = [False for _ in range(n)]
t2[0] = True

for i in range(n):
    if t2[i]:
        liczba = t1[i]
        dzielnik = 2
        while liczba > 1:
            if liczba % dzielnik == 0:
                if i + dzielnik < n:
                    t2[i + dzielnik] = True
                
                liczba /= dzielnik
            
            else:
                dzielnik += 1
        
if t2[n - 1]:
    print("da sie")

else:
    print("nie da sie")
