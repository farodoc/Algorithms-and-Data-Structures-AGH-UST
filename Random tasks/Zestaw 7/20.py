class Node:
    def __init__(self, val):
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

def combine(a, b):
    ap = a[0]
    ak = a[1]
    bp = b[0]
    bk = b[1]

    if bp <= ap and bk >= ak:
        return bp, bk
    
    elif ap <= bp and ak >= bk:
        return ap, ak

    elif bp <= ap and ap <= bk:
        return bp, ak

    else:
        return ap, bk

def czyNachodza(a, b):
    ap = a[0]
    ak = a[1]
    bp = b[0]
    bk = b[1]

    if ak < bp or bk < ap:
        return False

    return True

def przedzialy(p):
    if p is None or p.next is None:
        return p

    w = Node(None)
    w.next = p
    curr = p
    prev = p
    p = p.next

    while True:
        if curr.next is None:
            return w.next

        operacja = False
        while p is not None:
            if czyNachodza(curr.val, p.val):
                operacja = True
                curr.val = combine(curr.val, p.val)
                prev.next = p.next
                p = p.next

            else:
                prev = p
                p = p.next

        if not operacja:
            curr = curr.next
            prev = curr
            p = curr.next

        else:
            prev = curr
            p = curr.next

a = Node((1,2))
b = Node((4,113))
c = Node((11,15))

a.next = b
b.next = c

printList(a)
w = przedzialy(a)
printList(w)