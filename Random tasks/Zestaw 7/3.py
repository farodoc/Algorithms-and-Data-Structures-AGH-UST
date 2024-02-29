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

def scal(p1, p2):
    if p1 is None:
        return p2
    
    if p2 is None:
        return p1

    if p1.val > p2.val:
        w = p2
        p2 = p2.next

    else:
        w = p1
        p1 = p1.next

    res = w

    while p1 is not None and p2 is not None:
        if p1.val > p2.val:
            w.next = p2
            w = w.next
            p2 = p2.next
        
        else:
            w.next = p1
            w = w.next
            p1 = p1.next

    if p1 is None:
        w.next = p2
    
    else:
        w.next = p1

    return res

t1 = [2,3,5,7,11]
t2 = [1,3,4,7,8]

p1 = arrToList(t1)
p2 = arrToList(t2)

printList(p1)
printList(p2)

w = scal(p1, p2)

printList(w)