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

def reverse(p):
    if p is None:
        return p

    prev = None
    curr = p
    next = p.next

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

t = [1,2,3,4,4,4,44,1,2,3,213]

p = arrToList(t)
printList(p)
w = reverse(p)
printList(w)