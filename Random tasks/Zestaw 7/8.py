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

def eraseEvery2(p):
    if p is None:
        return p

    w = p

    while w.next is not None:
        if w.next.next is not None:
            w.next = w.next.next
            w = w.next
        
        else:
            w.next = None
            break

    return p 


t = [1,2,3,4,5,6,7,8]
p = arrToList(t)
printList(p)
w = eraseEvery2(p)
printList(w)