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

def erase(p):
    if p is None:
        return p
    
    if p.next is None:
        return None
    
    w = p

    while w.next is not None:
        prev = w
        w = w.next

    prev.next = None

    return p

t = [1,1,2,3,4]
p = arrToList(t)
printList(p)
w = erase(p)
printList(w)