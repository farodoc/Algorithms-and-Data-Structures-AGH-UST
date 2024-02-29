class Node:
    def __init__(self, val, last = None):
        self.val = val
        self.next = None

def arrToList(t):
    x = Node(None)
    res = x
    n = len(t)

    for i in range(n):
        x.next = Node(t[i])
        x = x.next

    return res.next

def printList(p):
    while p.next is not None:
        print(p.val, end = ', ')
        p = p.next

    print(p.val)

def odd1inBin(num):
    cnt = 0

    while num > 0:
        if num % 2 == 1:
            cnt += 1

        num //= 2

    return cnt % 2 == 1

def eraseOddBin(p):
    if p is None:
        return p

    w = Node(None)
    w.next = p
    p.last = w

    while p is not None:
        if odd1inBin(p.val):
            if p.next is None:
                p.last.next = None
                return w.next
            
            p.last.next = p.next
            p.next.last = p.last


        p = p.next

    return w.next

a = Node(8)
b = Node(3)
c = Node(5)
a.next = b
b.last = a
b.next = c
c.last = b

printList(a)
w = eraseOddBin(a)
printList(w)