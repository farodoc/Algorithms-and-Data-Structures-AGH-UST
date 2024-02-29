class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sort(l1, l2):
    head = Node(None)
    n = head
    while(l1.next != None and l2.next != None):
        if(l1.next.val > l2.next.val):
            n.next = l1.next
            l1.next = l1.next.next
        
        else:
            n.next = l2.next
            l2.next = l2.next.next
        
        n = n.next
    
    if l1.next != None:
        n.next = l1.next

    else:
        n.next = l2.next

    return head



#dana jest posortowana tablica t oraz liczba x. Napisac program ktory sprawdza czy istnieje takie indeksy i oraz j takie ze t[i] oraz t[j] daje sume x.

def findSum(t, x):
    n = len(t)
    left = 0
    right = n - 1

    while left < right:
        if t[left] + t[right] == x:
            return left, right
        
        if t[left] + t[right] > x:
            right -= 1
        
        else:
            left += 1

    return False


def water(t, A):
    def f(t, h):
        sum = 0
        n = len(t)
        for i in range(n):
            if t[i][1][1] < h:
                if t[i][0][1] < h:
                    sum += (t[i][1][0] - t[i][0][0]) * (t[i][0][1] - t[i][1][1])

                else:
                    sum += (t[i][1][0] - t[i][0][0]) * (h - t[i][1][1])

        return sum

    def minmaxH(t):
        minH = t[0][1][1]
        maxH = t[0][0][1]
        n = len(t)

        for i in range(1,n):
            if t[i][1][1] < minH:
                minH = t[i][1][1]
            
            if t[i][0][1] > maxH:
                maxH = t[i][0][1]

        return minH, maxH
        

    hTop = minmaxH(t)[1]
    hBot = minmaxH(t)[0]
    n = len(t)
    hMid = (hTop + hBot) / 2

    while hTop != hBot:
        hMid = (hTop + hBot) / 2
        res = f(t, hMid)
        if res == A:
            break

        if res > A:
            hTop = hMid - 1

        else:
            hBot = hMid + 1

    cnt = 0
    for i in range(n):
        if t[i][0][1] <= hMid:
            cnt += 1

    return cnt

t = [((1,5),(3,0)),((4,7),(7,6)),((9,9),(15,4))]

print(water(t,16))


#dana tablica t z liczbami naturalnymi. Czy istnieje liczba x (lider tablicy t), ktora wystepuje w ponad polowie miejsc.
def leader(t):
    num = t[0]
    cnt = 1
    n = len(t)
    for i in range(1, n):
        if num == t[i]:
            cnt += 1
        
        else:
            cnt -= 1
            if cnt == 0:
                num = t[i]
                cnt = 1

    if cnt == 0:
        return False
    
    cnt = 0
    for i in range(n):
        if t[i] == num:
            cnt += 1

    if cnt > n/2:
        return t[i]
    
    return False