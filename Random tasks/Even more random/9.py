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

def increment(p):
    if p is None:
        return

    w = p

    while w.next is not None:
        w = w.next

    w.val += 1

t = [1,2,0]
p = arrToList(t)
printList(p)
increment(p)
printList(p)