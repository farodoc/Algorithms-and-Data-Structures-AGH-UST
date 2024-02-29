class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def beforeCycle(p):
    p1 = p
    p2 = p
    p3 = p

    while True:
        p1 = p1.next
        p2 = p2.next.next
        
        if p1 == p2:
            break

    cycleLen = 1
    p1 = p1.next
    while p1 != p2:
        p1 = p1.next
        cycleLen += 1

    prev = p3
    p3 = p3.next

    while True:
        for _ in range(cycleLen):
            if p3 == p1:
                return prev
            p1 = p1.next
        prev = p3
        p3 = p3.next



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

print(beforeCycle(a).val)