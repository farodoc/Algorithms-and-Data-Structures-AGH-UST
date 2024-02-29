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

def eraseSmaller(p):
    w = Node(None)
    w.next = p
    prev = w

    if p is None or p.next is None:
        return p
    
    prev = p
    p = p.next

    while p is not None:
        if p.val < prev.val:
            if p.next is None:
                prev.next = None
                break

            else:
                prev.next = p.next

            p = p.next
            continue

        prev = p
        p = p.next

    return w.next

t = [1,2,1]
p = arrToList(t)
printList(p)
w = eraseSmaller(p)
printList(w)
        

    