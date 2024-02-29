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

def unikat(p, val):
    g = Node(val)

    if p is None:
        return g

    w = Node(None)
    w.next = p
    r = p
    prev = w

    while r is not None and r.val <= val:
        if r.val == val:
            if prev.next.next is None:
                prev.next = None

            else:
                prev.next = r.next

            return w.next
        
        prev = r
        r = r.next

    prev = w
    r = p

    while r is not None and r.val < val:
        prev = r
        r = r.next

    if prev.next is None:
        prev.next = g
        return w.next

    prev.next = g
    g.next = r

    return w.next

t = [2,3,5,7,11]
p = arrToList(t)
printList(p)
w = unikat(p,1)
printList(w)