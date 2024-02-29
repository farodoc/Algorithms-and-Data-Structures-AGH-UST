class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def isCycle(p):
    if p is None or p.next is None:
        return False

    p1 = p
    p2 = p

    while True:
        p1 = p1.next
        if p2.next is None or p2.next.next is None:
            return False

        p2 = p2.next.next

        if p1 == p2:
            return True

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d


print(isCycle(a))