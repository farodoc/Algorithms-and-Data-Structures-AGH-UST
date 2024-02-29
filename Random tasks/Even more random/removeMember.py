class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert(val, p):
    prev = None
    w = p
    while w is not None and w.val < val:
        prev = w
        w = w.next

    if w is not None and w.val == val:
        return p

    new = Node(val)
    new.next = w

    if prev is None:
        return

    prev.next = new
    return

def remove(val, p):
    prev = None
    w = p
    while w is not None and w.val < val:
        prev = w
        w = w.next

    if w.val > val:
        return

    prev.next = w.next

    return

    

def printList(p):
    while p.next is not None:
        print(p.val, end = ', ')
        p = p.next

    print(p.val)

a = Node(1)
b = Node(2)
c = Node(4)
d = Node(5)

a.next = b
b.next = c
c.next = d

printList(a)

insert(3,a)

printList(a)

remove(4,a)

printList(a)