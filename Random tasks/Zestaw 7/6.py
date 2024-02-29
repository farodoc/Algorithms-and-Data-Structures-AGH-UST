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

def add(p, val):
    w = p
    g = Node(val)

    if w is None:
        return g

    while w.next is not None:
        w = w.next

    w.next = g

    return p

t = [1]
p = None

w = add(p, 5)
printList(p)