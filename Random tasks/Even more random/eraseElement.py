class Node:
    def __init__(self,val):
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

def erase(p, num):
    guard = Node(None)
    guard.next = p
    prev = guard
    w = p

    if p is None:
        return p
    
    while w is not None and w.val < num:
        prev = w
        w = w.next

    if w is None or w.val > num:
        return p

    if w.next is None:
        prev.next = None
        return p

    prev.next = w.next
    return guard

t = [1,2,3,4]
p = arrToList(t)
printList(p)
erase(p,2)
printList(p)
    