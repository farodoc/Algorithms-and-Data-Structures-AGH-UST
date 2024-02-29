class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def cycleLen(p):
    p1 = p
    p2 = p

    while True:
        p1 = p1.next
        p2 = p2.next.next
        if p1 == p2:
            break

    cnt = 1
    p1 = p1.next
    while p1 != p2:
        cnt += 1
        p1 = p1.next

    return cnt

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = d

print(cycleLen(a))