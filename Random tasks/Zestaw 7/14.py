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

def eraseModulo(p):
    if p is None or p.next is None:
        return p

    w = Node(None)
    w.next = p
    prev = w

    while p.next is not None:
        if p.val % p.next.val == 0:
            prev.next = p.next
            p = p.next
            continue

        prev = p
        p = p.next

    return w.next

t = [2,1,3,5,6,3,4,3,1]
p = arrToList(t)
printList(p)
w = eraseModulo(p)
printList(w)